import pandas as pd
import numpy as np
import pickle
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import accuracy_score

def train_tuberculosis():
    df = pd.read_csv('diseases/datasets/tuberculosis.csv')
    # Example columns: age, cough, fever, weight_loss, night_sweats, result
    X = df.drop('result', axis=1)
    y = df['result']
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)
    accuracy = accuracy_score(y_test, model.predict(X_test))
    print(f"TB Model Accuracy: {accuracy:.2f}")
    with open('diseases/ml_models/tb_model.pkl', 'wb') as f:
        pickle.dump(model, f)

# Repeat for asthma, malaria, chickenpox, skin disease
# For image-based diseases (skin, chickenpox), use CNN or
# extract features from images using PIL before RandomForest

if __name__ == '__main__':
    train_tuberculosis()
    # train_asthma(), train_malaria(), etc.