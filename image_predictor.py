import numpy as np
import json
import os
from PIL import Image
import tensorflow as tf

IMG_SIZE = (224, 224)
CONFIDENCE_THRESHOLD = 0.60

_skin_model      = None
_chickenpox_model = None


def get_skin_model():
    global _skin_model
    if _skin_model is None:
        path = os.path.join('diseases', 'ml_models', 'skin_model.h5')
        if not os.path.exists(path):
            raise FileNotFoundError(f"Model not found: {path}")
        _skin_model = tf.keras.models.load_model(path)
    return _skin_model


def get_chickenpox_model():
    global _chickenpox_model
    if _chickenpox_model is None:
        path = os.path.join('diseases', 'ml_models', 'chickenpox_model.h5')
        if not os.path.exists(path):
            raise FileNotFoundError(f"Model not found: {path}")
        _chickenpox_model = tf.keras.models.load_model(path)
    return _chickenpox_model


def load_class_labels(disease_code):
    path_map = {
        'SKIN':  os.path.join('diseases', 'ml_models', 'skin_classes.json'),
        'CHKPX': os.path.join('diseases', 'ml_models',
                              'chickenpox_classes.json'),
    }
    path = path_map[disease_code]
    if not os.path.exists(path):
        raise FileNotFoundError(f"Class labels not found: {path}")
    with open(path, 'r') as f:
        labels = json.load(f)
    return {int(k): v for k, v in labels.items()}


# ─────────────────────────────────────────────────────────────────
# INVALID IMAGE DETECTION
# ─────────────────────────────────────────────────────────────────

def is_valid_medical_image(img):
    """
    Multi-layer validation to reject screenshots, documents,
    random photos, solid colors, and non-skin images.
    Returns (is_valid, reason)
    """
    arr = np.array(img, dtype=np.float32)
    h, w = arr.shape[:2]

    # ── 1. Size check ────────────────────────────────────────────
    if h < 80 or w < 80:
        return False, (
            "Image is too small. Please upload a higher "
            "resolution close-up photo of the affected area."
        )

    # ── 2. Blank / solid color check ─────────────────────────────
    std_dev = np.std(arr)
    if std_dev < 12:
        return False, (
            "Image appears blank or is a solid color. "
            "Please upload a real photo."
        )

    # ── 3. Too bright — white screenshot / blank page ─────────────
    mean_brightness = np.mean(arr)
    if mean_brightness > 235:
        return False, (
            "Image is too bright or appears to be a blank "
            "white screenshot. Please upload a real skin photo."
        )

    # ── 4. Too dark ───────────────────────────────────────────────
    if mean_brightness < 20:
        return False, (
            "Image is too dark to analyze. "
            "Please upload a well-lit photo."
        )

    # ── 5. Grayscale / screenshot detection ───────────────────────
    r = arr[:, :, 0]
    g = arr[:, :, 1]
    b = arr[:, :, 2]

    rg_diff = np.mean(np.abs(r.astype(float) - g.astype(float)))
    rb_diff = np.mean(np.abs(r.astype(float) - b.astype(float)))
    gb_diff = np.mean(np.abs(g.astype(float) - b.astype(float)))
    avg_color_diff = (rg_diff + rb_diff + gb_diff) / 3

    if avg_color_diff < 4.5:
        return False, (
            "Image appears to be a grayscale screenshot or "
            "document. Please upload a color photo of the "
            "affected skin area."
        )

    # ── 6. Screenshot detection — sharp edges / text-like regions ─
    # Screenshots typically have very uniform rows/columns
    row_std = np.std(np.mean(arr, axis=(1, 2)))
    col_std = np.std(np.mean(arr, axis=(0, 2)))
    if row_std < 2.5 and col_std < 2.5:
        return False, (
            "Image appears to be a screenshot or computer-generated "
            "image. Please upload a real photograph."
        )

    # ── 7. Skin tone check ────────────────────────────────────────
    # Real skin images have pixels where R > G > B (warm tones)
    # or at least have significant warm-tone presence
    r_mean = np.mean(r)
    g_mean = np.mean(g)
    b_mean = np.mean(b)

    # Check if image has at least some warm tones (skin-like pixels)
    warm_pixels = np.sum(
        (r > g) & (r > b) & (r > 60) & (r < 250)
    )
    total_pixels = h * w
    warm_ratio = warm_pixels / total_pixels

    # Very strict — at least 15% of pixels must be warm-toned
    if warm_ratio < 0.15:
        return False, (
            "The uploaded image does not appear to contain "
            "skin tissue. Please upload a clear close-up photo "
            "of the affected skin area (not a screenshot, "
            "diagram, or unrelated photo)."
        )

    # ── 8. High contrast text detection (UI screenshots) ──────────
    # Screenshots of apps/websites have high local contrast
    # in sharp rectangular patterns
    arr_gray = np.mean(arr, axis=2)
    local_diff = np.abs(
        np.diff(arr_gray, axis=0)
    ).mean() + np.abs(np.diff(arr_gray, axis=1)).mean()

    # If image has very high edge sharpness AND low color variation
    # it is likely a UI screenshot
    if local_diff > 35 and avg_color_diff < 10:
        return False, (
            "Image appears to be a UI screenshot or document scan. "
            "Please upload a real photograph of the skin condition."
        )

    return True, "OK"


def preprocess_image(image_file):
    """
    Opens, validates, resizes and normalizes the image.
    Returns (preprocessed_array, pil_image, is_valid, reason)
    """
    try:
        image_file.seek(0)
        img = Image.open(image_file).convert('RGB')
    except Exception as e:
        return None, None, False, (
            f"Could not open the file as an image: {str(e)}. "
            f"Please upload a valid JPG or PNG file."
        )

    # Run validation
    is_valid, reason = is_valid_medical_image(img)
    if not is_valid:
        return None, None, False, reason

    # Resize and normalize
    img_resized   = img.resize(IMG_SIZE)
    img_array     = np.array(img_resized, dtype=np.float32) / 255.0
    img_expanded  = np.expand_dims(img_array, axis=0)

    return img_expanded, img, True, "OK"


# ─────────────────────────────────────────────────────────────────
# SKIN DISEASE PREDICTOR
# ─────────────────────────────────────────────────────────────────

def predict_skin_disease(image_file):
    """
    Returns (predicted_label, confidence_percent, is_valid, message)
    """
    img_array, img, is_valid, reason = preprocess_image(image_file)
    if not is_valid:
        return None, 0.0, False, reason

    try:
        model        = get_skin_model()
        class_labels = load_class_labels('SKIN')
    except FileNotFoundError as e:
        return None, 0.0, False, str(e)
    except Exception as e:
        return None, 0.0, False, f"Model loading error: {str(e)}"

    try:
        predictions = model.predict(img_array, verbose=0)[0]
    except Exception as e:
        return None, 0.0, False, f"Prediction error: {str(e)}"

    max_confidence  = float(np.max(predictions))
    predicted_index = int(np.argmax(predictions))
    predicted_label = class_labels.get(predicted_index, 'Unknown')

    print(f"[SKIN] Predictions : {predictions}")
    print(f"[SKIN] Predicted   : {predicted_label} "
          f"({max_confidence * 100:.1f}%)")

    if max_confidence < CONFIDENCE_THRESHOLD:
        return None, round(max_confidence * 100, 2), False, (
            f"The image does not match any known skin condition "
            f"in our database. Best guess was '{predicted_label}' "
            f"with only {max_confidence * 100:.1f}% confidence. "
            f"Please upload a clearer, closer photo of the "
            f"affected skin area."
        )

    return predicted_label, round(max_confidence * 100, 2), True, "OK"


# ─────────────────────────────────────────────────────────────────
# CHICKENPOX PREDICTOR
# ─────────────────────────────────────────────────────────────────

def predict_chickenpox_disease(image_file):
    """
    Returns (predicted_label, confidence_percent, is_valid, message)
    """
    img_array, img, is_valid, reason = preprocess_image(image_file)
    if not is_valid:
        return None, 0.0, False, reason

    try:
        model        = get_chickenpox_model()
        class_labels = load_class_labels('CHKPX')
    except FileNotFoundError as e:
        return None, 0.0, False, str(e)
    except Exception as e:
        return None, 0.0, False, f"Model loading error: {str(e)}"

    try:
        predictions = model.predict(img_array, verbose=0)[0]
    except Exception as e:
        return None, 0.0, False, f"Prediction error: {str(e)}"

    max_confidence  = float(np.max(predictions))
    predicted_index = int(np.argmax(predictions))
    predicted_label = class_labels.get(predicted_index, 'Unknown')

    print(f"[CHKPX] Predictions : {predictions}")
    print(f"[CHKPX] Predicted   : {predicted_label} "
          f"({max_confidence * 100:.1f}%)")

    if max_confidence < CONFIDENCE_THRESHOLD:
        return None, round(max_confidence * 100, 2), False, (
            f"The image does not appear to show chickenpox symptoms. "
            f"Best guess was '{predicted_label}' with only "
            f"{max_confidence * 100:.1f}% confidence. "
            f"Please upload a clear photo of the rash or blisters."
        )

    return predicted_label, round(max_confidence * 100, 2), True, "OK"