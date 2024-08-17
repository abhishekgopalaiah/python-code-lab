class Graph:
    def __init__(self):
        self.graph_dict = {}

    def add_node(self, node):
        if node not in self.graph_dict:
            self.graph_dict[node] = []

    def add_edge(self, start, end):
        if start not in self.graph_dict:
            self.add_node(start)
        if end not in self.graph_dict:
            self.add_node(end)
        self.graph_dict[start].append(end)
        self.graph_dict[end].append(start)  # For undirected graph

    def display(self):
        for node, edges in self.graph_dict.items():
            print(f"{node}: {edges}")


if __name__ == '__main__':
    # Example usage
    graph = Graph()
    graph.add_edge('A', 'B')
    graph.add_edge('A', 'C')
    graph.add_edge('B', 'D')
    graph.add_edge('C', 'D')

    print("Graph:")
    graph.display()
