def read_dist_from_file(file_name: str):
    with open(file_name) as file:
        dist = int(file.readline())
    return dist


def read_heights_from_file(file_name: str):
    with open(file_name) as file:
        lines = file.readlines()
        heights = [int(height) for height in lines[1].split()]
    return heights


def write_res_to_file(file_name: str, res):
    res = float('{:.2f}'.format(res))
    with open(file_name, 'w') as file:
        file.write(str(res))