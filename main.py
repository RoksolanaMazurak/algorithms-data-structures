from file_manager import FileManager
from knight_tour import KnightTour

if __name__ == '__main__':
    file = FileManager()
    knight = KnightTour()
    start = file.get_start()
    end = file.get_finish()
    size = file.get_board_size()

    file.write_to_file(knight.min_knight_step(start, end, size))
