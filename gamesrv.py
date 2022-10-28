from queue import PriorityQueue

from vertex import Vertex
from graph import Graph


class GameSrv:
    def __init__(self, input_file: str, output_file: str):
        self.connection = Graph(input_file)
        self.output_file = output_file

    def dijkstra_shortest_path(self, start_vertex: Vertex):
        vertex_dist = {vertex: float('inf') for vertex in self.connection.vertices}
        vertex_dist[start_vertex] = 0

        pq = PriorityQueue()
        pq.put((0, start_vertex))
        while not pq.empty():
            dist, current_vertex = pq.get()
            for adjacent in current_vertex.get_adj_vertices():
                adjacent_vertex, edge_weight = adjacent

                prev_dist = vertex_dist[adjacent_vertex]
                new_dist = vertex_dist[current_vertex] + edge_weight

                if new_dist < prev_dist:
                    vertex_dist[adjacent_vertex] = vertex_dist[current_vertex] + edge_weight
                    pq.put((vertex_dist[adjacent_vertex], adjacent_vertex))
        return vertex_dist

    def get_min_max_latency(self):
        max_latency = []
        for vertex in self.connection.vertices:
            if vertex.value not in self.connection.client_vertex:
                current_vertex_dist = self.dijkstra_shortest_path(vertex)
                curr_latency_list = []
                for current_vertex, dist in current_vertex_dist.items():
                    if current_vertex.value in self.connection.client_vertex:
                        curr_latency_list.append(dist)
                max_latency.append(max(curr_latency_list))
        min_of_max_latency = min(max_latency)
        Graph.write_to_file(self.output_file, min_of_max_latency)
        return min(max_latency)


