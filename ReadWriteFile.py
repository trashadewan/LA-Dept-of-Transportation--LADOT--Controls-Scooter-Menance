import numpy as np


class ReadWriteFile:
    #  Read input file
    @staticmethod
    def read_input_file(file_name):
        # global n
        # global p
        # global s
        # global area
        # global reverse_index_list
        with open(file_name, 'r') as input_file:
            lines = input_file.readlines()
            n = int(lines[0].rstrip())  # number of grids
            p = int(lines[1].rstrip())  # number of police officers
            s = int(lines[2].rstrip())  # number of scooters
            total_no_of_lines = 12 * s + 3
            area = np.zeros([n, n], dtype=np.int16)
            for i in range(3, total_no_of_lines):
                x, y = lines[i].rstrip().split(",")
                area[int(x)][int(y)] = area[int(x)][int(y)] + 1
            reverse_index_list = np.unravel_index(np.argsort(area, axis=None)[::-1], area.shape)
        return n, p, area, reverse_index_list


    # print the final answer in the output_file
    @staticmethod
    def create_output_file(max):
        with open('output.txt', 'w') as output_file:
            output_file.write(max)
