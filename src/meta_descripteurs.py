import pandas as pd
import numpy as np
import networkx as nx

class MetaDescription:
    class Simple:

        @staticmethod
        def compute_graph_descriptors(G: nx.Graph) -> dict:
            is_connected = nx.is_connected(G.to_undirected()) if not G.is_directed() else nx.is_weakly_connected(G)

            descriptors = {
                'num_nodes': G.number_of_nodes(),
                'num_edges': G.number_of_edges(),
                'num_label_differents': len(set(nx.get_node_attributes(G, 'label').values())),
                'num_edge_labels': len(set(nx.get_edge_attributes(G, 'label').values())) if nx.get_edge_attributes(G, 'label') else 0,
                'max_distance': max(
                    (max(distance.values())
                    for node in G.nodes()
                    for distance in [nx.single_source_shortest_path_length(G, node)]),
                    default=0
                ),
                'density': nx.density(G),
                'num_connected_components': (
                    nx.number_connected_components(G.to_undirected())
                    if not G.is_directed()
                    else nx.number_weakly_connected_components(G)
                ),
                'diameter_if_connected': nx.diameter(G.to_undirected()) if is_connected else 0
            }

            return descriptors

        @staticmethod
        def compute_graph_descriptor_all(graphs: list[tuple[nx.Graph, int]]) -> pd.DataFrame:
            """Calcule les descripteurs pour une liste de graphes avec labels arbitraires (int ou str)."""
            descriptors = [
                {**MetaDescription.Simple.compute_graph_descriptors(graph[0]), 'label': graph[1]}
                for graph in graphs
            ]
            return pd.DataFrame.from_records(descriptors)
        
    class Statistics:

        @staticmethod
        def compute_data_statistics(data: pd.DataFrame) -> pd.DataFrame:
            stats = {
                'min': data.min(numeric_only=True),
                'kurtosis': data.kurtosis(numeric_only=True),
                'skewness': data.skew(numeric_only=True),
                'std': data.std(numeric_only=True),
                'mean': data.mean(numeric_only=True),
                'max': data.max(numeric_only=True),
            }
            return pd.DataFrame(stats).T.replace([np.inf, -np.inf, np.nan], 0)