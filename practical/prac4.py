# Breadth First Search

class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

def printLevel(root, height):
    if root is None:
        return
    if(height == 1):
        print(root.key)
        height = height + 1
        printLevel(root.left, height)
        printLevel(root.right, height)
    elif(height > 1):
        print(root.key)
        height = height + 1
        printLevel(root.left, height)
        printLevel(root.right, height)

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

printLevel(root, 1)