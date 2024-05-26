import networkx as nx
import matplotlib.pyplot as plt

class Screen:
    def __init__(self):
        self.graph = nx.DiGraph()
    

    def add_node(self, node):
        self.graph.add_node(node)
    

    def add_edge(self, origin, destination):
        self.graph.add_edge(origin, destination);

    def draw(self):
        plt.clf()
        pos = nx.shell_layout(self.graph)
        nx.draw(self.graph, pos, with_labels=True, font_weight='bold', node_size=1000)