from vertex import Vertex


class Graph:
    def __init__(self, input_file):
        self.vertices = []
        self.__read_input(input_file)

    def __read_input(self, input_file):
        with open(input_file) as file:
            lines = file.readlines()
        self.vertex_num = int(lines[0].split()[0])
        self.edges_num = int(lines[0].split()[1])
        self.client_vertex = [int(client_vertex) for client_vertex in lines[1].split()]

        for n in range(self.edges_num):
            start_vertex, end_vertex, edge_weight = lines[n + 2].split(" ")
            start = Vertex(start_vertex)
            end = Vertex(end_vertex)
            start = self.__vertex_in_list(start)
            end = self.__vertex_in_list(end)
            start, end, weight = [int(edge) for edge in lines[n + 2].split()]
            start_vertex = Vertex(start)
            end_vertex = Vertex(end)

            if self.__vertex_in_list(start_vertex) is None:
                start_vertex.add_adj_vertices(end_vertex if self.__vertex_in_list(end_vertex) is None
                                              else self.__vertex_in_list(end_vertex), weight)
                self.vertices.append(start_vertex)
            else:
                vertex = self.__vertex_in_list(start_vertex)
                vertex.add_adj_vertices(end_vertex if self.__vertex_in_list(end_vertex) is None
                                        else self.__vertex_in_list(end_vertex), weight)

            if self.__vertex_in_list(end_vertex) is None:
                end_vertex.add_adj_vertices(start_vertex if self.__vertex_in_list(start_vertex) is None
                                            else self.__vertex_in_list(start_vertex), weight)
                self.vertices.append(end_vertex)
            else:
                vertex = self.__vertex_in_list(end_vertex)
                vertex.add_adj_vertices(start_vertex if self.__vertex_in_list(start_vertex) is None
                                        else self.__vertex_in_list(start_vertex), weight)

    def __vertex_in_list(self, cur_vertex: Vertex):
        for vertex in self.vertices:
            if cur_vertex == vertex:
                return vertex
        return None

    def write_to_file(output: str, value: int):
        with open(output, "w") as file:
            file.write(str(value))
