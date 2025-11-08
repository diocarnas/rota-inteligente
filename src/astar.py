# src/astar.py
import networkx as nx
from typing import List, Any, Tuple
import math

def euclidean_heuristic(u: Any, v: Any, G: nx.Graph) -> float:
    """
    Heurística baseada em distância euclidiana entre posições armazenadas nos nós (lat, lon).
    Retorna 0 se posições não existirem.
    """
    du = G.nodes.get(u, {})
    dv = G.nodes.get(v, {})
    if 'lat' in du and 'lon' in du and 'lat' in dv and 'lon' in dv:
        # converter lat/lon para plano aproximado (não ótimo para longas distâncias)
        dx = du['lon'] - dv['lon']
        dy = du['lat'] - dv['lat']
        return math.hypot(dx, dy)
    return 0.0

def shortest_path_astar(G: nx.Graph, source: Any, target: Any) -> Tuple[List[Any], float]:
    """
    Usa NetworkX A* se possível; fallback para Dijkstra se heurística não aplicável.
    Retorna (path, cost).
    """
    try:
        h = lambda a, b: euclidean_heuristic(a, b, G)
        path = nx.astar_path(G, source, target, heuristic=h, weight='weight')
        cost = nx.path_weight(G, path, weight='weight')
        return path, cost
    except Exception as e:
        # fallback
        path = nx.dijkstra_path(G, source, target, weight='weight')
        cost = nx.path_weight(G, path, weight='weight')
        return path, cost
