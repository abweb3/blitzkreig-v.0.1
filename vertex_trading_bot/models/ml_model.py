"""
Machine Learning Model for Price Prediction
"""

import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.preprocessing import StandardScaler


class MLModel:
    def __init__(self, features, lookback, prediction_horizon):
        self.features = features
        self.lookback = lookback
        self.prediction_horizon = prediction_horizon
        self.model = RandomForestRegressor(n_estimators=100, random_state=42)
        self.scaler = StandardScaler()

    def prepare_data(self, df):
        X = df[self.features].values
        y = (
            df["close"]
            .pct_change(self.prediction_horizon)
            .shift(-self.prediction_horizon)
            .values
        )
        X = self.scaler.fit_transform(X)
        return X[: -self.prediction_horizon], y[: -self.prediction_horizon]

    def train(self, df):
        X, y = self.prepare_data(df)
        self.model.fit(X, y)

    def predict(self, current_data):
        X = self.scaler.transform(current_data[self.features].values.reshape(1, -1))
        return self.model.predict(X)[0]
