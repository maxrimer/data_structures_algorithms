# creating a graph using adjacency list

class Graph:
    def __init__(self):
        self.adjacency_list = {}

    def add_vertex(self, vertex):
        if vertex not in self.adjacency_list.keys():
            self.adjacency_list[vertex] = []
            return True
        return False

    def print_graph(self):
        for vertex in self.adjacency_list:
            print(vertex, ':', self.adjacency_list[vertex])

    def add_edge(self, vertex1, vertex2):
        if vertex1 in self.adjacency_list.keys() and vertex2 in self.adjacency_list.keys():
            self.adjacency_list[vertex1].append(vertex2)
            self.adjacency_list[vertex2].append(vertex1)
            return True
        return False

    def remove_edge(self, vertex1, vertex2):
        if vertex1 in self.adjacency_list.keys() and vertex2 in self.adjacency_list.keys():
            try:
                self.adjacency_list[vertex1].remove(vertex2)
                self.adjacency_list[vertex2].remove(vertex1)
                return True
            except ValueError:
                return 'The edge between given vertices does not exist'
        return False

    def remove_vertex(self, vertex):
        if vertex in self.adjacency_list.keys():
            for other_vertices in self.adjacency_list[vertex]:
                self.adjacency_list[other_vertices].remove(vertex)
            del self.adjacency_list[vertex]
            return True
        return False

    # Traversing a graph
    def bfs(self, vertex):
        if vertex in self.adjacency_list.keys():
            visited = [vertex]
            queue = [vertex]
            while queue:
                devertex = queue.pop(0)
                print(devertex)
                for neighbor_vertex in self.adjacency_list[devertex]:
                    if neighbor_vertex not in visited:
                        visited.append(neighbor_vertex)
                        queue.append(neighbor_vertex)
        else:
            return False

    def dfs(self, vertex):
        if vertex in self.adjacency_list.keys():
            visited = [vertex]
            stack = [vertex]

            while stack:
                stacked = stack.pop()
                print(stacked)
                for adjacent_vertex in self.adjacency_list[stacked]:
                    if adjacent_vertex not in visited:
                        visited.append(adjacent_vertex)
                        stack.append(adjacent_vertex)
        else:
            return False


graph = Graph()
graph.add_vertex('A')
graph.add_vertex('B')
graph.add_vertex('C')
graph.add_vertex('D')
graph.add_vertex('E')
graph.add_vertex('F')
graph.add_vertex('G')
graph.add_edge('A', 'B')
graph.add_edge('A', 'D')
graph.add_edge('B', 'C')
graph.add_edge('D', 'F')
graph.add_edge('D', 'G')
graph.add_edge('C', 'E')
graph.add_edge('E', 'G')
# print(graph.remove_edge('A', 'C'))
graph.print_graph()
# print('removing vertex...')
# print(graph.remove_vertex('B'))
# graph.print_graph()
# graph.bfs('B')
graph.dfs('A')