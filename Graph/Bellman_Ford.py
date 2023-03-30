# Bellman-Ford algorithm for SSSP problem

class Graph:
    def __init__(self, num_of_vert):
        self.num_of_vert = num_of_vert
        self.node = []
        self.edge = []

    def add_edge(self, s, d, w):
        self.edge.append([s, d, w])

    def add_node(self, value):
        self.node.append(value)

    def print_solution(self, dist):
        print('Vertex distance from source')
        for k,v in dist.items():
            print('   ' + k, ' :    ', v)

    def bellman_ford(self, src):
        dist = {i: float('inf') for i in self.node}
        dist[src] = 0

        for _ in range(self.num_of_vert - 1):
            for s, d, w in self.edge:
                if dist[s] != float('inf') and dist[s] + w < dist[d]:
                    dist[d] = dist[s] + w

        for s, d, w in self.edge:
            if dist[s] != float('inf') and dist[s] + w < dist[d]:
                print('There is a negative cycle in a graph')
                return

        self.print_solution(dist)


g = Graph(5)
g.add_node('A')
g.add_node('B')
g.add_node('C')
g.add_node('D')
g.add_node('E')

g.add_edge('A', 'C', 6)
g.add_edge('A', 'D', 6)
g.add_edge('B', 'A', 3)
g.add_edge('C', 'D', 1)
g.add_edge('D', 'C', 2)
g.add_edge('D', 'B', 1)
g.add_edge('E', 'B', 4)
g.add_edge('E', 'D', 2)
g.bellman_ford('E')




















