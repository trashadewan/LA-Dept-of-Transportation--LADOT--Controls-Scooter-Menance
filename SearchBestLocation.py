import numpy as np
import Queue
import time
import copy
from Node import Node
from ReadWriteFile import ReadWriteFile


# check if the state exists in our explored dict
def exists_in_explored_list(state, explored_listQ):
    if state in explored_listQ:
        return True
    return False


# check if the state exists in our frontier Priority Queue
def exists_in_frontier(marshal_value, frontier):
    l = frontier.queue
    length = len(l)
    for i in range(0, length):
        if l[i].marshalValue == marshal_value:
            return True
    return False


# check if queen is allowed for this state
def queen_allowed(list_queen, x, y):
    length = len(list_queen)
    if length > 0:
        for l in range(0, length):
            if list_queen[l][0] == x:
                return False
            if list_queen[l][1] == y:
                return False
            if abs(list_queen[l][0] - x) == abs(list_queen[l][1] - y):
                return False
        return True
    else:
        return True


def search_best_location(area, best_solution, explored_list, frontier, max, n, p, reverse_index_list):
    while not frontier.empty():
        currentNode = Node(None, 0, 0, area, 0, [])
        currentNode.copy(frontier.get())
        explored_list[currentNode.marshalValue] = 1
        if currentNode.depth == p:
            if max < currentNode.g:
                max = currentNode.g
                best_solution.copy(currentNode)
            continue
        children = []
        length = len(reverse_index_list[0])
        for i in range(currentNode.pointer, length):
            if currentNode.depth + length - i == p:
                continue
            x = reverse_index_list[0][i]
            y = reverse_index_list[1][i]
            possible_sum = currentNode.g
            if best_solution.g > 0:
                min_no = min(i + p - currentNode.depth, n * n)
                for increment in range(i, min_no):
                    a = reverse_index_list[0][increment]
                    b = reverse_index_list[1][increment]
                    possible_sum += area[a][b]
                if best_solution.g >= possible_sum:
                    break
            if queen_allowed(currentNode.queen_positions, x, y):
                state = np.copy(currentNode.state)
                state[x][y] = -1
                queen_positions = copy.copy(currentNode.queen_positions)
                queen_positions.append((x, y))
                newNode = Node(currentNode, 1, currentNode.state[x][y], state, currentNode.pointer + 1, queen_positions)
                children.append(newNode)
        for child in children:
            if exists_in_explored_list(child.marshalValue, explored_list):
                continue
            if exists_in_frontier(child.marshalValue, frontier):
                continue
            frontier.put(child)
    return max


def main(file):
    # start Program
    n, p, area, reverse_index_list = ReadWriteFile.read_input_file(file)
    # Initialize both frontier Queue and Explored dict
    frontier = Queue.PriorityQueue()
    explored_list = {}
    # start node is initialized
    start = Node(None, 0, 0, area, 0, [])
    frontier.put(start)
    max = 0
    best_solution = Node(None, 0, 0, area, 0, [])
    max = search_best_location(area, best_solution, explored_list, frontier, max, n, p, reverse_index_list)
    ReadWriteFile.create_output_file(str(max))
    print max
    print "Frontier len " + str(len(frontier.queue))
    print "Explored List Q " + str(len(explored_list))


if __name__ == '__main__':
    t = int(time.time() * 1000)
    main('input.txt')
    print "Time taken len " + str(int(time.time() * 1000) - t)