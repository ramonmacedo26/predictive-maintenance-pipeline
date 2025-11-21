import pandas as pd
import matplotlib.pyplot as plt

PROCESSED_PATH = "data/processed/sensors_clean.csv"

df = pd.read_csv(PROCESSED_PATH)

print("[EDA] Estatísticas:")
print(df.describe())

plt.figure(figsize=(10,5))
plt.plot(df["timestamp"], df["temperature"])
plt.title("Temperatura ao longo do tempo")
plt.xlabel("Tempo")
plt.ylabel("Temperatura")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
