from collections import defaultdict


class Graph:
    def __init__(self, graphsize):
        self.adjacency_list = defaultdict(list)
        self.graphsize = graphsize

    def add_edge(self, v, edge):
        self.adjacency_list[v].append(edge)

    # Topological sort
    def topologicalsort_util(self, v, visited, stack):
        visited.append(v)

        for dependent_node in self.adjacency_list[v]:
            if dependent_node not in visited:
                self.topologicalsort_util(dependent_node, visited, stack)

        stack.insert(0, v)

    def topologicalsort(self):
        visited = []
        stack = []

        for k in list(self.adjacency_list):
            if k not in visited:
                self.topologicalsort_util(k, visited, stack)

        print(stack)


customgraph = Graph(8)
customgraph.add_edge('A', 'C')
customgraph.add_edge('C', 'E')
customgraph.add_edge('E', 'H')
customgraph.add_edge('E', 'F')
customgraph.add_edge('F', 'G')
customgraph.add_edge('B', 'D')
customgraph.add_edge('B', 'C')
customgraph.add_edge('D', 'F')

customgraph.topologicalsort()


















