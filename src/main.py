# src/main.py
import argparse
from src.graph import sample_graph, load_graph_from_csv
from src.astar import shortest_path_astar
from src.clustering import load_deliveries, kmeans_cluster_deliveries
from src.visualize import plot_graph, plot_clusters
import os

def run_demo():
    # Gera grafo de exemplo
    G = sample_graph()
    print("Nós do grafo:", list(G.nodes()))
    # Encontra rota A* entre Restaurante e BairroB
    path, cost = shortest_path_astar(G, "Restaurante", "BairroB")
    print("Caminho A*:", path, " Custo:", cost)
    plot_graph(G, path=path, save_path="docs/grafo_demo.png")
    print("Grafo demo salvo em docs/grafo_demo.png")

def run_with_files(edge_csv: str, deliveries_csv: str, k: int):
    G = load_graph_from_csv(edge_csv)
    print("Grafo carregado com", len(G.nodes), "nós e", len(G.edges), "arestas.")
    # exemplo: rota entre dois nós (ajuste conforme seus dados)
    nodes = list(G.nodes())
    if len(nodes) >= 2:
        source = nodes[0]
        target = nodes[-1]
        path, cost = shortest_path_astar(G, source, target)
        print(f"Caminho A* de {source} a {target} -> {path} (custo {cost})")
        os.makedirs("docs", exist_ok=True)
        plot_graph(G, path=path, save_path="docs/grafo_from_csv.png")
        print("Grafo plotado em docs/grafo_from_csv.png")

    # clustering
    df = load_deliveries(deliveries_csv)
    df_clustered, km = kmeans_cluster_deliveries(df, k)
    print("Distribuição por cluster:")
    print(df_clustered['cluster'].value_counts())
    plot_clusters(df_clustered, save_path="docs/clusters.png")
    print("Clusters plotados em docs/clusters.png")
    df_clustered.to_csv("docs/deliveries_clustered.csv", index=False)
    print("Deliveries com clusters salvos em docs/deliveries_clustered.csv")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Rota Inteligente - Demo")
    parser.add_argument("--edges", help="CSV de arestas (mapa).", default=None)
    parser.add_argument("--deliveries", help="CSV de entregas (lat,lon).", default=None)
    parser.add_argument("--k", type=int, help="Número de clusters (entregadores).", default=2)
    args = parser.parse_args()

    if args.edges and args.deliveries:
        run_with_files(args.edges, args.deliveries, args.k)
    else:
        run_demo()
