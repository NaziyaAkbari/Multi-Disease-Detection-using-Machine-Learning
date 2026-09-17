# 🏥 Multi Disease Detection Using Machine Learning

## 📌 About the Project

**MedDetect AI** is an intelligent web-based disease detection system that uses
Machine Learning and Deep Learning to provide preliminary screening for
five major diseases prevalent in India.

The system uses two detection approaches:
- **Symptom-Based** (Tuberculosis, Malaria, Asthma) — 10 weighted questions per disease
- **Image-Based** (Skin Disease, Chickenpox) — MobileNetV2 CNN with Transfer Learning

> ⚠️ This is a **screening and awareness tool only**.
> Always consult a qualified doctor for proper medical diagnosis.



## 🦠 Diseases Covered

| Disease | Detection Method | Algorithm |
|---|---|---|
| Tuberculosis | Symptom-Based | Weighted Scoring |
| Malaria | Symptom-Based | Weighted Scoring |
| Asthma | Symptom-Based | Weighted Scoring |
| Skin Disease | Image-Based | MobileNetV2 CNN |
| Chickenpox | Image + Symptom | MobileNetV2 CNN |


## 🛠️ Tech Stack

| Layer | Technology |
|---|---|
| Language | Python 3.10 |
| Web Framework | Django 5.2 |
| Deep Learning | TensorFlow 2.x, Keras, MobileNetV2 |
| Machine Learning | Scikit-learn, Random Forest |
| Data Processing | Pandas, NumPy |
| Image Processing | Pillow (PIL) |
| Frontend | HTML5, CSS3, Bootstrap 5, JavaScript |
| Database | SQLite 3 |
| Visualization | Matplotlib |
| Email | Gmail SMTP |
| IDE | Visual Studio Code |


## 📁 Project Structure

multi-disease-detection/
│
├── disease_detection/ # Django project settings
│ ├── settings.py
│ ├── urls.py
│ └── wsgi.py
│
├── accounts/ # User registration and login
│ ├── models.py # UserProfile model
│ ├── views.py
│ └── urls.py
│
├── diseases/ # All 5 disease prediction modules
│ ├── models.py # PredictionRecord, ContactMessage
│ ├── views.py # All prediction logic
│ ├── urls.py
│ ├── image_predictor.py # CNN prediction + image validation
│ ├── disease_data.py # Medicines, tips, hospitals data
│ └── ml_models/ # Trained .h5 model files
│ ├── skin_model.h5
│ ├── skin_classes.json
│ ├── chickenpox_model.h5
│ └── chickenpox_classes.json
│
├── dashboard/ # Admin dashboard
│ ├── views.py
│ └── urls.py
│
├── templates/ # All HTML templates
│ ├── base.html
│ ├── landing.html
│ ├── about.html
│ ├── contact.html
│ ├── accounts/
│ ├── diseases/
│ └── dashboard/
│
├── static/ # CSS and JS files
├── media/ # Uploaded images
├── requirements.txt
└── manage.py


## Author: NAZIYA AKBARI
