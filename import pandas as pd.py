import pandas as pd
import numpy as np
import joblib

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import (
    mean_absolute_error,
    mean_squared_error,
    r2_score
)

sales = pd.read_csv(
    "data/feature_engineered_sales.csv"
)

X = sales[
    [
        "Day",
        "Month",
        "Week",
        "Weekend",
        "M01AB_Lag1",
        "M01AB_MA7"
    ]
]

y = sales["M01AB"]

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

model = RandomForestRegressor(random_state=42)

model.fit(X_train, y_train)

predictions = model.predict(X_test)

print("MAE:",
      mean_absolute_error(y_test, predictions))

print("RMSE:",
      np.sqrt(mean_squared_error(y_test, predictions)))

print("R2:",
      r2_score(y_test, predictions))

joblib.dump(model, "model.pkl")

print("Model Saved Successfully!")