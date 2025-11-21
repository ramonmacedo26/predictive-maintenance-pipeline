import pandas as pd
import sqlite3
from datetime import datetime

RAW_PATH = "data/raw/sensors.csv"
PROCESSED_PATH = "data/processed/sensors_clean.csv"
DB_PATH = "database/warehouse.db"

def extract():
    print("[EXTRACT] Lendo arquivo CSV...")
    df = pd.read_csv(RAW_PATH)
    return df

def transform(df):
    print("[TRANSFORM] Limpando dados...")
    df["timestamp"] = pd.to_datetime(df["timestamp"])
    df = df.dropna()
    return df

def load(df):
    print("[LOAD] Salvando dados tratados...")
    df.to_csv(PROCESSED_PATH, index=False)

    conn = sqlite3.connect(DB_PATH)
    df.to_sql("sensors", conn, if_exists="replace", index=False)
    conn.close()

if __name__ == "__main__":
    df_raw = extract()
    df_clean = transform(df_raw)
    load(df_clean)
    print("[DONE] Pipeline ETL executado com sucesso!")
