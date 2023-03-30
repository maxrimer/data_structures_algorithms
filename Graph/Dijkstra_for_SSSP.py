# class for edges
import heapq


class Edge:
    def __init__(self, weight, start_vertex, target_vertex):
        self.weight = weight
        self.start_vertex = start_vertex
        self.target_vertex = target_vertex


class Node:
    def __init__(self, name):
        self.name = name
        self.visited = False
        self.predecessor = None
        # Adjacent nodes
        self.neighbors = []
        # Initial value for distance
        self.min_distance = float('inf')

    def __lt__(self, other_node):
        return self.min_distance < other_node.min_distance

    def add_edge(self, weight, destination):
        edge = Edge(weight, self, destination)
        self.neighbors.append(edge)


class Dijkstra:
    def __init__(self):
        self.heap = []

    def calculate(self, start_vertex):
        start_vertex.min_distance = 0
        heapq.heappush(self.heap, start_vertex)
        while self.heap:
            actual_vertex = heapq.heappop(self.heap)
            if actual_vertex.visited:
                continue
            for edge in actual_vertex.neighbors:
                start = edge.start_vertex
                target = edge.target_vertex
                curr_distance = start.min_distance + edge.weight
                if curr_distance < target.min_distance:
                    target.min_distance = curr_distance
                    target.predecessor = actual_vertex
                    heapq.heappush(self.heap, target)
            actual_vertex.visited = True

    def get_shortest_path(self, vertex):
        print(f'The distance to vertex {vertex.name} is {vertex.min_distance}')
        actual_vertex = vertex
        while actual_vertex:
            print(actual_vertex.name, end=' ')
            actual_vertex = actual_vertex.predecessor


# Creating Nodes
nodeA = Node('A')
nodeB = Node('B')
nodeC = Node('C')
nodeD = Node('D')
nodeE = Node('E')
nodeF = Node('F')
nodeG = Node('G')
nodeH = Node('H')

# Creating Edges
nodeA.add_edge(6, nodeB)
nodeA.add_edge(9, nodeD)
nodeA.add_edge(10, nodeC)
nodeB.add_edge(5, nodeD)
nodeB.add_edge(13, nodeF)
nodeB.add_edge(16, nodeE)
nodeD.add_edge(8, nodeF)
nodeD.add_edge(7, nodeH)
nodeF.add_edge(4, nodeE)
nodeF.add_edge(12, nodeG)
nodeE.add_edge(10, nodeG)
nodeH.add_edge(2, nodeF)
nodeH.add_edge(14, nodeG)
nodeC.add_edge(6, nodeD)
nodeC.add_edge(5, nodeH)
nodeC.add_edge(21, nodeG)


algorithm = Dijkstra()
algorithm.calculate(nodeA)
algorithm.get_shortest_path(nodeG)











