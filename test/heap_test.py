import sys

sys.path.append('/root/projects/obify')

from obify import heap

class Node():
    def __init__(self, data):
        self.data = data

    def compare(self, node):
        if self.data < node.data:
            return -1
        elif self.data > node.data:
            return 1
        else:
            return 0

def test_heap():
    h = heap.MinHeap()
    h.insert(Node(12))
    h.insert(Node(2))
    h.insert(Node(20))
    h.insert(Node(1))
    h.insert(Node(0))
    h.remove()
    #h.remove()
    printall(h)

def printall(h):
    for element in h.getall():
        print(element.data)

test_heap()
