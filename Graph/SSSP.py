# Single source shortest path using bfs algorithm

class Graph:
    def __init__(self, gdict=None):
        if not gdict:
            self.gdict = {}
        self.gdict = gdict

    def bfs_for_sssp(self, start, end):
        queue = [[start]]

        while queue:
            path = queue.pop(0)
            last_node = path[-1]
            if last_node == end:
                return path
            for adjacent_node in self.gdict.get(last_node, []):
                new_path = list(path)
                new_path.append(adjacent_node)
                queue.append(new_path)


customdict = {
    'a': ['b', 'c'],
    'b': ['d', 'g'],
    'c': ['d', 'e'],
    'd': ['f'],
    'e': ['f'],
    'g': ['f']
}

g = Graph(customdict)
print(g.bfs_for_sssp('a', 'e'))
