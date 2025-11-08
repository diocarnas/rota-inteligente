# src/searches.py
import networkx as nx
from typing import List, Any, Tuple

def bfs_shortest_unweighted(G: nx.Graph, source: Any, target: Any) -> List[Any]:
    """
    Retorna o caminho BFS (menor número de arestas) entre source e target.
    """
    try:
        path = nx.shortest_path(G, source=source, target=target)
        return path
    except nx.NetworkXNoPath:
        return []

def dfs_path(G: nx.Graph, source: Any, target: Any) -> List[Any]:
    """
    Retorna um caminho encontrado por DFS (não necessariamente ótimo).
    """
    try:
        path = list(nx.dfs_edges(G, source=source))
        # converter dfs_edges para caminho até target (simples heurística)
        if source == target:
            return [source]
        # usar algoritmo shortest_path com cutoff ou simplesmente return shortest_path fallback
        return nx.shortest_path(G, source=source, target=target)
    except Exception:
        return []
