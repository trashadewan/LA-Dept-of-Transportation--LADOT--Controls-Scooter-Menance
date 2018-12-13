import marshal

# Node class for maintaining nodes in the Algorithm Tree
class Node:
    def __init__(self, parent, depth, g, state, pointer, queen_positions):
        self.parent = parent
        self.depth = depth
        if parent is None:
            self.depth = depth
            self.g = g
        else:
            self.depth = parent.depth + depth
            self.g = parent.g + g
        self.state = state
        self.pointer = pointer
        self.marshalValue = marshal.dumps(self.state)
        self.queen_positions = queen_positions

    def __eq__(self, compare):
        return self.depth > compare.depth

    def __cmp__(self, other):
        return cmp(-1 * self.g, -1 * other.g)

    def display(self):
        if self.parent is not None:
            print self.parent.state
        print self.depth
        print self.g
        print self.state
        print self.pointer
        print self.queen_positions

    def copy(self, copy_from):
        self.parent = copy_from.parent
        self.depth = copy_from.depth
        self.g = copy_from.g
        self.state = copy_from.state
        self.pointer = copy_from.pointer
        self.marshalValue = copy_from.marshalValue
        self.queen_positions = copy_from.queen_positions
