class Vertex:
    def __init__(self, value):
        self.value = value
        self.adjacent_vertex = set()

    def __eq__(self, v):
        return self.value == v.value

    def __hash__(self):
        return hash(int(self.value))

    def __lt__(self, v):
        return self.value < v.value

    def __gt__(self, v):
        return self.value > v.value

    def add_adj_vertices(self, adjacent, edge_weight: int):
        self.adjacent_vertex.add((adjacent, edge_weight))

    def get_adj_vertices(self):
        return self.adjacent_vertex



