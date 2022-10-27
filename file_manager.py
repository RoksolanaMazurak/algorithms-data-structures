class FileManager:

    def get_board_size(self):
        with open('resource/input.txt') as rf:
            size = int(rf.readline())
        return size

    def get_start(self):
        start_coord = [None] * 2
        with open('resource/input.txt') as rf:

            for i in range(1, 4):
                content = int(rf.readline())
                if i == 2:
                    start_coord[0] = content

                if i == 3:
                    start_coord[1] = content
        return start_coord

    def get_finish(self):
        finish_coord = [None] * 2
        with open('resource/input.txt') as rf:

            for i in range(1, 6):
                content = int(rf.readline())

                if i == 4:
                    finish_coord[0] = content

                if i == 5:
                    finish_coord[1] = content
        return finish_coord

    def write_to_file(self, level: int):
        with open('resource/output.txt', 'w') as wf:
            wf.write(str(level))
