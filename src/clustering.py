# src/clustering.py
import pandas as pd
import numpy as np
from sklearn.cluster import KMeans
from typing import Tuple

def load_deliveries(csv_path: str) -> pd.DataFrame:
    """
    CSV esperado com colunas: order_id, lat, lon, other...
    """
    df = pd.read_csv(csv_path)
    if not {'lat', 'lon'}.issubset(df.columns):
        raise ValueError("CSV de entregas deve conter colunas 'lat' e 'lon'.")
    return df

def kmeans_cluster_deliveries(df: pd.DataFrame, k: int, random_state: int = 42) -> Tuple[pd.DataFrame, KMeans]:
    coords = df[['lat', 'lon']].to_numpy()
    km = KMeans(n_clusters=k, random_state=random_state)
    labels = km.fit_predict(coords)
    df_out = df.copy()
    df_out['cluster'] = labels
    return df_out, km
