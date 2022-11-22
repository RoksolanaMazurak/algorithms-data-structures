from longest_cable_length import find_longest_cable_length
from file_manager import write_res_to_file, read_dist_from_file, read_heights_from_file

cable = find_longest_cable_length(read_dist_from_file('resource/input1.txt'), read_heights_from_file(
    'resource/input1.txt'))
write_res_to_file('resource/output1.txt', cable)

cable = find_longest_cable_length(read_dist_from_file('resource/input2.txt'), read_heights_from_file(
    'resource/input2.txt'))
write_res_to_file('resource/output2.txt', cable)

cable = find_longest_cable_length(read_dist_from_file('resource/input3.txt'), read_heights_from_file(
    'resource/input3.txt'))
write_res_to_file('resource/output3.txt', cable)
