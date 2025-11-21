import pandas as pd

PROCESSED_PATH = "data/processed/sensors_clean.csv"
OUT_PATH = "data/processed/sensors_features.csv"

df = pd.read_csv(PROCESSED_PATH)

df["temp_change"] = df["temperature"].diff().fillna(0)
df["pressure_change"] = df["pressure"].diff().fillna(0)
df["vibration_change"] = df["vibration"].diff().fillna(0)

df.to_csv(OUT_PATH, index=False)
print("[FEATURE ENGINEERING] Variáveis criadas com sucesso!")
