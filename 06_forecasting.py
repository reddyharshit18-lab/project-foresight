import pandas as pd
import joblib

model = joblib.load("model.pkl")

future = pd.DataFrame({

    "Day":[1],

    "Month":[7],

    "Week":[27],

    "Weekend":[0],

    "M01AB_Lag1":[11],

    "M01AB_MA7":[10.5]

})

prediction = model.predict(future)

print("Tomorrow Forecast:")

print(prediction)