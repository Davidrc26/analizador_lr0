import networkx as nx
import matplotlib.pyplot as plt

class Screen:
    def __init__(self):
        self.graph = nx.Graph()
    

    def add_node(self, node):
        self.graph.add_node(node)
    

    def add_edge(self, origin, destination):
        self.graph.add_edge(origin, destination);

    def draw(self):
        plt.clf()
        nx.draw(self.graph, with_labels=True, font_weight='bold')