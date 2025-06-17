import networkx as nx

from meta_descripteurs import MetaDescription

def random_graph_with_labels(num_nodes: int, num_edges: int, labels: list) -> nx.Graph:
    """Génère un graphe aléatoire avec des labels pour les nœuds."""
    G = nx.gnm_random_graph(num_nodes, num_edges)
    for i, node in enumerate(G.nodes()):
        G.nodes[node]['label'] = labels[i % len(labels)]
    return G

EXEMPLE_DATASET = [
    (random_graph_with_labels(5, 4, ['A', 'B', 'C']), 0),
    (random_graph_with_labels(8, 6, ['A', 'B', 'C']), 1),
    (random_graph_with_labels(10, 12, ['A', 'B', 'C']), 1),
    (random_graph_with_labels(6, 5, ['A', 'B', 'C']), 1),
    (random_graph_with_labels(9, 8, ['A', 'B', 'C']), 1),
    (random_graph_with_labels(4, 3, ['A', 'B', 'C']), 1),
    (random_graph_with_labels(11, 10, ['A', 'B', 'C']), 2),
    (random_graph_with_labels(7, 7, ['A', 'B', 'C']), 2),
    (random_graph_with_labels(13, 14, ['A', 'B', 'C']), 0)
]

META_DESCRIPTEURS = MetaDescription.Simple.compute_graph_descriptor_all(EXEMPLE_DATASET)
print(META_DESCRIPTEURS)
META_DESCRIPTEURS_STAT = MetaDescription.Statistics.compute_data_statistics(META_DESCRIPTEURS)
print(META_DESCRIPTEURS_STAT)