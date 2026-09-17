import pickle
import numpy as np

def load_model(disease_code):
    model_map = {
        'TB':    'diseases/ml_models/tb_model.pkl',
        'ASTH':  'diseases/ml_models/asthma_model.pkl',
        'MAL':   'diseases/ml_models/malaria_model.pkl',
        'CHKPX': 'diseases/ml_models/chickenpox_model.pkl',
        'SKIN':  'diseases/ml_models/skin_model.pkl',
    }
    with open(model_map[disease_code], 'rb') as f:
        return pickle.load(f)

def predict_disease(disease_code, features):
    model = load_model(disease_code)
    features_array = np.array(features).reshape(1, -1)
    prediction = model.predict(features_array)[0]
    confidence = max(model.predict_proba(features_array)[0]) * 100
    return prediction, round(confidence, 2)