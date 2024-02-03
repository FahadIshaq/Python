import networkx as nx
import matplotlib.pyplot as plt

# Define the edges and their capacities and flows
edges = {
    ('s', 'a'): {'capacity': 10, 'flow': 7},
    ('s', 'c'): {'capacity': 10, 'flow': 8},
    ('a', 'b'): {'capacity': 7, 'flow': 3},
    ('b', 't'): {'capacity': 10, 'flow': 6},
    ('c', 'a'): {'capacity': 5, 'flow': 0},
    ('c', 'd'): {'capacity': 10, 'flow': 8},
    ('c', 'e'): {'capacity': 5, 'flow': 0},
    ('d', 't'): {'capacity': 15, 'flow': 12},
    ('e', 'd'): {'capacity': 5, 'flow': 0},
    ('e', 't'): {'capacity': 5, 'flow': 0},
}

# Create a directed graph
G = nx.DiGraph()

# Add nodes and edges to the graph
for edge, data in edges.items():
    # Add the forward edge with the residual capacity
    G.add_edge(edge[0], edge[1], capacity=data['capacity'] - data['flow'])
    # Add the backward edge with a capacity equal to the flow (if flow is greater than zero)
    if data['flow'] > 0:
        G.add_edge(edge[1], edge[0], capacity=data['flow'])

# Draw the residual graph
pos = nx.spring_layout(G)  # positions for all nodes

# nodes
nx.draw_networkx_nodes(G, pos, node_size=700)

# edges
nx.draw_networkx_edges(G, pos, width=6)
nx.draw_networkx_labels(G, pos, font_size=20, font_family="sans-serif")

edge_labels = {(u, v): f"{d['capacity']}" for u, v, d in G.edges(data=True)}
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)

# Labels and titles
plt.title('Residual Graph Gf')
plt.axis('off')  # Turn off the axis
plt.show()  # Display the residual graph
