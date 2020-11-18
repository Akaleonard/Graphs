# Singly Linked List
class ListNode:
    def __init__(self, value):
        self.value = value

        self.next = None

        # self.prev if DLL
## LL Traversal
current = node
while current is not None:
    current = current.next

class BinarySearchTreeNode:
    self.value = value

    self.left = None
    self.right = None

# BST Traversal
# DFT, BFT
### Stack, Queue

while node is not None: 
    recurse(self.left)
    recurse(self.right)

class GraphNode:
    def __init__(self, value):
        self.value = "B"

        # options: dictionary, array, set
        # B's connections
        self.connections = set("A", "C", "D")

        # A's connections
        self.connections = set("B")

        # D's connections
        self.connections = set()

# outbound vs inbound connections        

## Graph Traversals

## DFT, stack
### Check every node once, check every connection once

# make a stack
stack = Stack("B")
# make a set to track visited
visited = set("A")

# put the start node into the stack

# while the stack isn't empty

# pop off the top of the stack, this is our current node
current_node = "A"

# Check if we visited this node yet
## if not, add to our visited set

# and add each of its neighbors to our stack

# BFT, queue
q = Queue()

# make a set to track visited
visited = set()

# enqueue the start node

# while our queue isn't empty

# dequeue from front of line, this is our current node
current_node = "A"

# check if we've visited here yet
## if not, add to visited
## get its neighbors, for each, add to stack
neighbors = set()