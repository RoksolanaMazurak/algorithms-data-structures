from cell import Cell


class KnightTour:

    def is_on_board(self, x, y, board_size):
        if 0 <= x <= board_size and 0 <= y <= board_size:
            return True
        return False

    def min_knight_step(self, start_coord, finish_coord, board_size):
        row = [2, 2, -2, -2, 1, 1, -1, -1]
        col = [1, -1, 1, -1, 2, -2, 2, -2]

        queue = [Cell(start_coord[0], start_coord[1], 0)]

        visited = [[False for i in range(board_size + 1)]
                   for j in range(board_size + 1)]

        visited[start_coord[0]][start_coord[1]] = True

        while queue:

            vertex = queue[0]
            queue.pop(0)

            if (vertex.x == finish_coord[0] and
                    vertex.y == finish_coord[1]):
                return vertex.level

            for i in range(8):

                x = vertex.x + row[i]
                y = vertex.y + col[i]

                if (self.is_on_board(x, y, board_size)
                        and not visited[x][y]):
                    visited[x][y] = True
                    queue.append(Cell(x, y, vertex.level + 1))
        return -1
