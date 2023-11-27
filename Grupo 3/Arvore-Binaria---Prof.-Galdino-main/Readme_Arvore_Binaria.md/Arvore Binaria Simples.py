

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def __str__(self):
        return str(self.data)
    
class BinaryTree:
    def __init__(self, data):
        node = Node(data)
        self.root = node

if __name__ == "__main__":
    tree = BinaryTree(9)
    tree.root.left = Node (17)
    tree.root.right = Node (3)

    print(tree.root)
    print(tree.root.left)