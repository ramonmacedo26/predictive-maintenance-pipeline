import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression

DATA_PATH = "data/processed/sensors_features.csv"

df = pd.read_csv(DATA_PATH)

df["target"] = df["status"].apply(lambda x: 1 if x == "FAILURE" else 0)

X = df[["temperature", "pressure", "vibration", "temp_change", "pressure_change"]]
y = df["target"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

model = LogisticRegression()
model.fit(X_train, y_train)

print("[MODEL] Acurácia:", model.score(X_test, y_test))
