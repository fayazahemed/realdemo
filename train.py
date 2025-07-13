import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import joblib

df = pd.read_csv("insurance_data.csv")

# Preprocessing
df['Gender'] = df['Gender'].map({'Male': 0, 'Female': 1})
df['Vehicle_Type'] = df['Vehicle_Type'].map({'Car': 0, 'Motorcycle': 1, 'Truck': 2})

X = df.drop("Claim", axis=1)
y = df["Claim"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = RandomForestClassifier()
model.fit(X_train, y_train)

joblib.dump(model, "model.pkl")
