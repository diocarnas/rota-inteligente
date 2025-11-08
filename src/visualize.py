# src/visualize.py
import networkx as nx
import matplotlib.pyplot as plt
from .graph import node_positions
import pandas as pd

def plot_graph(G: nx.Graph, path=None, save_path: str = None):
    pos = node_positions(G)
    if not pos:
        pos = nx.spring_layout(G)
    plt.figure(figsize=(8,6))
    nx.draw(G, pos=pos, with_labels=True, node_size=500)
    if path:
        edges_in_path = list(zip(path[:-1], path[1:]))
        nx.draw_networkx_edges(G, pos=pos, edgelist=edges_in_path, width=3)
    if save_path:
        plt.savefig(save_path, bbox_inches='tight')
    else:
        plt.show()

def plot_clusters(df_with_clusters, save_path: str = None):
    plt.figure(figsize=(7,6))
    groups = df_with_clusters.groupby('cluster')
    for name, group in groups:
        plt.scatter(group['lon'], group['lat'], label=f'cluster {name}', s=20)
    plt.xlabel('Longitude')
    plt.ylabel('Latitude')
    plt.legend()
    if save_path:
        plt.savefig(save_path, bbox_inches='tight')
    else:
        plt.show()
