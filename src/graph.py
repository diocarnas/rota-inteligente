# src/graph.py
import networkx as nx
import pandas as pd
from typing import Tuple

def load_graph_from_csv(edge_csv_path: str) -> nx.Graph:
    """
    Espera um CSV com colunas: source,target,weight,src_lat,src_lon,tgt_lat,tgt_lon (lat/lon opcional)
    Retorna um NetworkX Graph com pesos 'weight' e atributos de posição (lat, lon) se presentes.
    """
    df = pd.read_csv(edge_csv_path)
    G = nx.Graph()
    for _, row in df.iterrows():
        u = row['source']
        v = row['target']
        w = float(row['weight'])
        G.add_edge(u, v, weight=w)
        # armazena posição de nós, se existirem
        if 'src_lat' in row and 'src_lon' in row:
            if u not in G.nodes:
                G.add_node(u, lat=float(row['src_lat']), lon=float(row['src_lon']))
            if v not in G.nodes:
                G.add_node(v, lat=float(row['tgt_lat']), lon=float(row['tgt_lon']))
    return G

def sample_graph() -> nx.Graph:
    """
    Gera um grafo pequeno de exemplo (para testes) com atributos de lat/lon.
    """
    G = nx.Graph()
    G.add_node("Restaurante", lat=-23.5505, lon=-46.6333)
    G.add_node("Centro", lat=-23.5510, lon=-46.6345)
    G.add_node("BairroA", lat=-23.5480, lon=-46.6350)
    G.add_node("BairroB", lat=-23.5525, lon=-46.6360)
    G.add_edge("Restaurante", "Centro", weight=3)
    G.add_edge("Restaurante", "BairroA", weight=8)
    G.add_edge("Centro", "BairroB", weight=2)
    G.add_edge("BairroA", "BairroB", weight=4)
    return G

def node_positions(G: nx.Graph):
    """
    Retorna um dicionário nodo -> (lon, lat) para plot.
    """
    pos = {}
    for n, d in G.nodes(data=True):
        lat = d.get('lat')
        lon = d.get('lon')
        if lat is not None and lon is not None:
            pos[n] = (lon, lat)
    return pos
