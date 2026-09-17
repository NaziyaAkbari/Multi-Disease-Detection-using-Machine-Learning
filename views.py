import json
import os
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.mail import EmailMultiAlternatives, send_mail
from django.conf import settings
from urllib3 import request
from .models import PredictionRecord, ContactMessage          # ← both here
from .disease_data import DISEASE_DATA, DEFAULT_HOSPITALS
from .image_predictor import predict_skin_disease, predict_chickenpox_disease

def landing(request):
    if request.user.is_authenticated:
        return redirect('disease_home')
    return render(request, 'landing.html')

# ── Skin disease labels shown on form ────────────────────────────
SKIN_DISEASE_LABELS = [
    'Acne', 'Eczema', 'Melanoma',
    'Psoriasis', 'Ringworm', 'Rosacea',
    'Seborrheic Dermatitis', 'Vitiligo',
]

# ─────────────────────────────────────────────────────────────────
# HELPERS
# ─────────────────────────────────────────────────────────────────

def simple_predict(features):
    """Symptom-based prediction using majority voting."""
    score = sum(features)
    total = len(features)
    if total == 0:
        return 'Negative', 0.0
    confidence = round((score / total) * 100, 2)
    prediction = 'Positive' if score >= (total / 2) else 'Negative'
    return prediction, confidence


def get_result_context(disease_code, disease_name,
                       prediction, confidence, location):
    """Build context dict for symptom-based result.html."""
    data = DISEASE_DATA.get(disease_code, {})
    if prediction == 'Positive':
        medicines = data.get('medicines_positive', [])
        tips      = data.get('tips_positive', [])
        hospitals = data.get('hospitals', {}).get(location, DEFAULT_HOSPITALS)
    else:
        medicines = []
        tips      = data.get('tips_negative', [])
        hospitals = []
    return {
        'disease':    disease_name,
        'prediction': prediction,
        'confidence': confidence,
        'location':   location,
        'medicines':  medicines,
        'tips':       tips,
        'hospitals':  hospitals,
    }


def get_image_result_context(disease_code, disease_name,
                             predicted_label, confidence, location):
    """Build context dict for image-based image_result.html."""
    data = DISEASE_DATA.get(disease_code, {})
    # Anything that is not 'normal' or 'healthy' is treated as positive
    is_positive = predicted_label.lower() not in ['normal', 'healthy']
    if is_positive:
        medicines = data.get('medicines_positive', [])
        tips      = data.get('tips_positive', [])
        hospitals = data.get('hospitals', {}).get(location, DEFAULT_HOSPITALS)
    else:
        medicines = []
        tips      = data.get('tips_negative', [])
        hospitals = []
    return {
        'disease':         disease_name,
        'predicted_label': predicted_label,
        'confidence':      confidence,
        'location':        location,
        'medicines':       medicines,
        'tips':            tips,
        'hospitals':       hospitals,
        'is_positive':     is_positive,
    }


def save_symptom_record(user, disease_type, post_data,
                        prediction, confidence):
    """Save a symptom-based prediction to the database."""
    # Convert QueryDict to plain dict safely
    data_dict = {}
    for key, value in post_data.items():
        data_dict[key] = value
    # Remove csrf token before saving
    data_dict.pop('csrfmiddlewaretoken', None)

    PredictionRecord.objects.create(
        user=user,
        disease_type=disease_type,
        input_data=json.dumps(data_dict),
        prediction=prediction,
        confidence=confidence,
    )


def save_image_record(user, disease_type, predicted_label,
                      confidence, image=None):
    """Save an image-based prediction to the database."""
    PredictionRecord.objects.create(
        user=user,
        disease_type=disease_type,
        input_data=json.dumps({
            'label':  predicted_label,
            'method': 'image',
        }),
        prediction=predicted_label,
        confidence=confidence,
        uploaded_image=image,
    )


# ─────────────────────────────────────────────────────────────────
# HOME
# ─────────────────────────────────────────────────────────────────

@login_required
def home(request):
    return render(request, 'diseases/home.html')


# ── Replace simple_predict with this new version ─────────────────

def symptom_predict(features, weights=None):
    """
    Weighted symptom prediction.
    weights: list of importance values per symptom (default all 1)
    Returns (prediction, confidence, raw_score)
    """
    if weights is None:
        weights = [1] * len(features)

    weighted_score = sum(f * w for f, w in zip(features, weights))
    max_score      = sum(weights)

    if max_score == 0:
        return 'Negative', 0.0, 0.0

    confidence = round((weighted_score / max_score) * 100, 2)

    if confidence >= 70:
        prediction = 'Positive'
    elif confidence >= 40:
        prediction = 'Uncertain'
    else:
        prediction = 'Negative'

    return prediction, confidence, weighted_score


def get_result_context(disease_code, disease_name,
                       prediction, confidence, location):
    data = DISEASE_DATA.get(disease_code, {})

    if prediction == 'Positive':
        medicines = data.get('medicines_positive', [])
        tips      = data.get('tips_positive', [])
        hospitals = data.get('hospitals', {}).get(
            location, DEFAULT_HOSPITALS)
        similar_diseases = []

    elif prediction == 'Uncertain':
        medicines = []
        tips      = data.get('tips_positive', [])
        hospitals = data.get('hospitals', {}).get(
            location, DEFAULT_HOSPITALS)
        similar_diseases = data.get('similar_diseases', [])

    else:
        medicines        = []
        tips             = data.get('tips_negative', [])
        hospitals        = []
        similar_diseases = []

    return {
        'disease':          disease_name,
        'prediction':       prediction,
        'confidence':       confidence,
        'location':         location,
        'medicines':        medicines,
        'tips':             tips,
        'hospitals':        hospitals,
        'similar_diseases': similar_diseases,
    }


# ── TUBERCULOSIS ─────────────────────────────────────────────────
@login_required
def tuberculosis_predict(request):
    if request.method == 'POST':
        # Weighted symptoms — key TB indicators get higher weight
        features = [
            int(request.POST.get('persistent_cough', 0)),
            int(request.POST.get('coughing_blood', 0)),
            int(request.POST.get('chest_pain', 0)),
            int(request.POST.get('fever_evening', 0)),
            int(request.POST.get('night_sweats', 0)),
            int(request.POST.get('unexplained_weight_loss', 0)),
            int(request.POST.get('extreme_fatigue', 0)),
            int(request.POST.get('loss_of_appetite', 0)),
            int(request.POST.get('shortness_breath', 0)),
            int(request.POST.get('swollen_lymph_nodes', 0)),
        ]
        # TB-specific weights
        # coughing blood and swollen lymph nodes are very specific to TB
        weights = [2, 4, 2, 2, 3, 3, 1, 1, 1, 3]

        location = request.POST.get('location', '')
        prediction, confidence, _ = symptom_predict(features, weights)

        save_symptom_record(
            request.user, 'TB', request.POST, prediction, confidence)

        context = get_result_context(
            'TB', 'Tuberculosis', prediction, confidence, location)
        return render(request, 'diseases/result.html', context)

    return render(request, 'diseases/tuberculosis_form.html')


# ── MALARIA ──────────────────────────────────────────────────────
@login_required
def malaria_predict(request):
    if request.method == 'POST':
        features = [
            int(request.POST.get('high_fever_sudden', 0)),
            int(request.POST.get('cyclical_fever', 0)),
            int(request.POST.get('chills_rigors', 0)),
            int(request.POST.get('profuse_sweating', 0)),
            int(request.POST.get('severe_headache', 0)),
            int(request.POST.get('nausea_vomiting', 0)),
            int(request.POST.get('muscle_joint_pain', 0)),
            int(request.POST.get('anaemia_pallor', 0)),
            int(request.POST.get('enlarged_spleen', 0)),
            int(request.POST.get('recent_travel_endemic', 0)),
        ]
        # Cyclical fever, rigors, travel history are
        # very specific to Malaria
        weights = [2, 4, 3, 2, 2, 1, 2, 2, 3, 4]

        location = request.POST.get('location', '')
        prediction, confidence, _ = symptom_predict(features, weights)

        save_symptom_record(
            request.user, 'MAL', request.POST, prediction, confidence)

        context = get_result_context(
            'MAL', 'Malaria', prediction, confidence, location)
        return render(request, 'diseases/result.html', context)

    return render(request, 'diseases/malaria_form.html')


# ── ASTHMA ───────────────────────────────────────────────────────
@login_required
def asthma_predict(request):
    if request.method == 'POST':
        features = [
            int(request.POST.get('wheezing_sound', 0)),
            int(request.POST.get('shortness_breath_exertion', 0)),
            int(request.POST.get('chest_tightness', 0)),
            int(request.POST.get('night_cough', 0)),
            int(request.POST.get('cold_triggered_cough', 0)),
            int(request.POST.get('exercise_worsens', 0)),
            int(request.POST.get('allergy_history', 0)),
            int(request.POST.get('family_asthma_history', 0)),
            int(request.POST.get('dust_smoke_trigger', 0)),
            int(request.POST.get('inhaler_relief', 0)),
        ]
        # Wheezing + inhaler relief are most specific to Asthma
        weights = [4, 3, 3, 2, 2, 2, 2, 2, 1, 4]

        location = request.POST.get('location', '')
        prediction, confidence, _ = symptom_predict(features, weights)

        save_symptom_record(
            request.user, 'ASTH', request.POST, prediction, confidence)

        context = get_result_context(
            'ASTH', 'Asthma', prediction, confidence, location)
        return render(request, 'diseases/result.html', context)

    return render(request, 'diseases/asthma_form.html')

# ─────────────────────────────────────────────────────────────────
# CHICKENPOX  (image + symptom)
# ─────────────────────────────────────────────────────────────────

@login_required
def chickenpox_predict(request):
    if request.method == 'POST':
        location = request.POST.get('location', '')
        image    = request.FILES.get('chickenpox_image')

        # ── Image path ──────────────────────────────────────────
        if image:
            predicted_label, confidence, is_valid, msg = \
                predict_chickenpox_disease(image)

            if not is_valid:
                return render(request, 'diseases/invalid_image.html', {
                    'disease': 'Chickenpox',
                    'reason':  msg,
                })

            save_image_record(
                request.user, 'CHKPX',
                predicted_label, confidence, image
            )

            context = get_image_result_context(
                'CHKPX', 'Chickenpox',
                predicted_label, confidence, location
            )
            return render(request, 'diseases/image_result.html', context)

        # ── Symptom path ────────────────────────────────────────
        features = [
            int(request.POST.get('itchy_spots', 0)),
            int(request.POST.get('fever', 0)),
            int(request.POST.get('headache', 0)),
            int(request.POST.get('fatigue', 0)),
            int(request.POST.get('loss_of_appetite', 0)),
        ]
        prediction, confidence = simple_predict(features)

        save_symptom_record(
            request.user, 'CHKPX', request.POST,
            prediction, confidence
        )

        context = get_result_context(
            'CHKPX', 'Chickenpox',
            prediction, confidence, location
        )
        return render(request, 'diseases/result.html', context)

    return render(request, 'diseases/chickenpox_form.html')


# ─────────────────────────────────────────────────────────────────
# SKIN DISEASE  (image only)
# ─────────────────────────────────────────────────────────────────

@login_required
def skin_predict(request):
    if request.method == 'POST':
        location = request.POST.get('location', '')
        image    = request.FILES.get('skin_image')

        # No image uploaded
        if not image:
            messages.error(request, 'Please upload a skin image.')
            return render(request, 'diseases/skin_form.html', {
                'disease_labels': SKIN_DISEASE_LABELS
            })

        # Run image predictor
        predicted_label, confidence, is_valid, msg = \
            predict_skin_disease(image)

        # Invalid image
        if not is_valid:
            return render(request, 'diseases/invalid_image.html', {
                'disease': 'Skin Disease',
                'reason':  msg,
            })

        # Save record
        save_image_record(
            request.user, 'SKIN',
            predicted_label, confidence, image
        )

        # Build context and show result
        context = get_image_result_context(
            'SKIN', 'Skin Disease',
            predicted_label, confidence, location
        )
        return render(request, 'diseases/image_result.html', context)

    # GET request — show the form
    return render(request, 'diseases/skin_form.html', {
        'disease_labels': SKIN_DISEASE_LABELS
    })


# ─────────────────────────────────────────────────────────────────
# PREDICTION HISTORY
# ─────────────────────────────────────────────────────────────────

@login_required
def prediction_history(request):
    records = PredictionRecord.objects.filter(
        user=request.user
    ).order_by('-created_at')
    return render(request, 'diseases/history.html', {
        'records': records
    })
# ─────────────────────────────────────────────────────────────────
# ABOUT US
# ─────────────────────────────────────────────────────────────────
def about(request):
    return render(request, 'about.html')


# ─────────────────────────────────────────────────────────────────
# CONTACT US
# ─────────────────────────────────────────────────────────────────
def contact(request):
    message_sent = False
    error        = None

    if request.method == 'POST':
        name    = request.POST.get('name', '').strip()
        email   = request.POST.get('email', '').strip()
        subject = request.POST.get('subject', '').strip()
        msg     = request.POST.get('message', '').strip()

        if name and email and subject and msg:

            # 1 — Save to database
            ContactMessage.objects.create(
                name=name,
                email=email,
                subject=subject,
                message=msg
            )

            # 2 — Send email to naziyaakbari7@gmail.com
            try:
                html_body = f"""
<div style="font-family:Arial,sans-serif;max-width:600px;margin:auto;
            border:1px solid #ddd;border-radius:12px;overflow:hidden;">
  <div style="background:#1a1a2e;padding:24px;text-align:center;">
    <h2 style="color:white;margin:0;">New Contact Message</h2>
    <p style="color:#adb5bd;margin:6px 0 0;">MedDetect AI Platform</p>
  </div>
  <div style="padding:28px;">
    <table style="width:100%;border-collapse:collapse;margin-bottom:20px;">
      <tr>
        <td style="padding:10px;background:#f8f9fa;
                   font-weight:bold;width:28%;">Name</td>
        <td style="padding:10px;border-bottom:1px solid #eee;">
          {name}
        </td>
      </tr>
      <tr>
        <td style="padding:10px;background:#f8f9fa;font-weight:bold;">
          Email
        </td>
        <td style="padding:10px;border-bottom:1px solid #eee;">
          <a href="mailto:{email}" style="color:#2980b9;">{email}</a>
        </td>
      </tr>
      <tr>
        <td style="padding:10px;background:#f8f9fa;font-weight:bold;">
          Subject
        </td>
        <td style="padding:10px;border-bottom:1px solid #eee;">
          {subject}
        </td>
      </tr>
    </table>
    <div style="background:#f8f9fa;border-left:4px solid #1a1a2e;
                padding:16px;border-radius:6px;margin-bottom:24px;">
      <p style="font-weight:bold;margin:0 0 8px;">Message:</p>
      <p style="margin:0;color:#444;line-height:1.8;">{msg}</p>
    </div>
    <div style="text-align:center;">
      <a href="mailto:{email}?subject=Re: {subject}"
         style="background:#1a1a2e;color:white;padding:12px 28px;
                border-radius:8px;text-decoration:none;
                font-weight:bold;display:inline-block;">
        Reply to {name}
      </a>
    </div>
  </div>
  <div style="background:#f8f9fa;padding:12px;text-align:center;
              color:#888;font-size:12px;border-top:1px solid #eee;">
    +91 7019050568 | Kalaburagi, Karnataka 585103<br>
    Sent from MedDetect AI Contact Form
  </div>
</div>"""

                plain_body = (
                    f"New contact message — MedDetect AI\n\n"
                    f"Name   : {name}\n"
                    f"Email  : {email}\n"
                    f"Subject: {subject}\n\n"
                    f"Message:\n{msg}"
                )

                # Email to you (naziyaakbari7@gmail.com)
                admin_email = EmailMultiAlternatives(
                    subject=f'[MedDetect AI] {subject} — from {name}',
                    body=plain_body,
                    from_email=settings.DEFAULT_FROM_EMAIL,
                    to=['naziyaakbari7@gmail.com'],
                    reply_to=[email],
                )
                admin_email.attach_alternative(html_body, "text/html")
                admin_email.send(fail_silently=False)

                # Confirmation email to sender
                send_mail(
                    subject='We received your message — MedDetect AI',
                    message=(
                        f"Hi {name},\n\n"
                        f"Thank you for contacting MedDetect AI!\n"
                        f"We received your message and will reply within "
                        f"1-2 business days.\n\n"
                        f"Your message: {msg}\n\n"
                        f"Best regards,\n"
                        f"MedDetect AI Team\n"
                        f"naziyaakbari7@gmail.com | +91 7019050568"
                    ),
                    from_email=settings.DEFAULT_FROM_EMAIL,
                    recipient_list=[email],
                    fail_silently=True,
                )

                message_sent = True

            except Exception as e:
                print(f"[EMAIL ERROR] {str(e)}")
                message_sent = True
                error = (
                    "Your message was saved but email delivery failed. "
                    f"Error: {str(e)}"
                )

    return render(request, 'contact.html', {
        'message_sent': message_sent,
        'error':        error,
    })