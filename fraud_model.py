import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier


def train_fraud_model():

    np.random.seed(42)

    data = pd.DataFrame({
        "amount": np.random.randint(100, 20000, 500),
        "frequency": np.random.randint(1, 10, 500),
        "country_risk": np.random.randint(1, 3, 500),
        "new_beneficiary": np.random.randint(0, 2, 500),
    })

    data["fraud"] = (
        (data["amount"] > 10000) |
        (data["frequency"] > 7) |
        (data["new_beneficiary"] == 1)
    ).astype(int)

    X = data.drop("fraud", axis=1)
    y = data["fraud"]

    model = RandomForestClassifier()
    model.fit(X, y)

    return model


model = train_fraud_model()


def predict_risk(amount, frequency, country, new_beneficiary):

    country_map = {
        "USA": 1,
        "UAE": 2,
        "Singapore": 1
    }

    country_risk = country_map[country]

    input_data = [[amount, frequency, country_risk, new_beneficiary]]

    prediction = model.predict(input_data)[0]

    return "High" if prediction == 1 else "Low"