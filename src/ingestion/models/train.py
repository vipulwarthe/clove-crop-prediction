import joblib
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
from src.utils.config import Config

def train_model(X, y):
    X = X.reshape(X.shape[0], -1).T

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2
    )

    model = RandomForestClassifier(n_estimators=100)

    model.fit(X_train, y_train)

    preds = model.predict(X_test)

    print(classification_report(y_test, preds))

    joblib.dump(model, Config.MODEL_PATH)

    print("Model saved at:", Config.MODEL_PATH)