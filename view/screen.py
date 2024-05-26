import networkx as nx
import matplotlib.pyplot as plt


class Screen:
    def __init__(self):
        self.graph = nx.DiGraph()

    def add_node(self, node):
        self.graph.add_node(node, color="#add8e6")

    def add_edge(self, origin, destination, label):
        self.graph.add_edge(origin, destination, label=label )

    def draw(self):
        plt.clf()
        colors = [self.graph.nodes[node].get(
            'color', 'blue') for node in self.graph.nodes]
        pos = nx.spiral_layout(self.graph)
        nx.draw(self.graph, pos, node_color=colors, with_labels=True,
                font_weight='bold', node_size=1000)
        edge_labels = nx.get_edge_attributes(self.graph, 'label')
        nx.draw_networkx_edge_labels(self.graph, pos, edge_labels=edge_labels)
        

    def paintAcceptance(self, state):
        self.graph.nodes[state]["color"] = "green"
        self.draw()

    def paintSinks(self):
        sinks = [node for node, outdegree in self.graph.out_degree()
                 if outdegree == 0]
        for sink in sinks:
            self.paintAcceptance(sink)
