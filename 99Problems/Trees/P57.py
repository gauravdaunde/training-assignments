'''
Binary search trees (dictionaries)
    Use the predicate add/3, developed in chapter 4 of the course, to write a predicate to construct a binary search tree from a list of integer numbers.
    Example:
    * construct([3,2,5,7,1],T).
    T = t(3, t(2, t(1, nil, nil), nil), t(5, nil, t(7, nil, nil)))

    Then use this predicate to test the solution of the problem P56.
    Example:
    * test-symmetric([5,3,18,1,4,12,21]).
    Yes
    * test-symmetric([3,2,5,7,1]).
    No
'''


class BinaryTree:
    def __init__(self, data=None):
        self.data = data
        self.left = None
        self.right = None

    def addNode(self, data):  # method that add nodes
        if self.data == None:
            self.data = data
        if self.data > data:
            if self.left == None:
                self.left = BinaryTree(data)
            else:
                self.left.addNode(data)
        if self.data < data:
            if self.right == None:
                self.right = BinaryTree(data)
            else:
                self.right.addNode(data)


# returns binary tree created with nodes_list
def createTree(nodes_list):
    binary_tree = BinaryTree()

    for node in nodes_list:
        binary_tree.addNode(node)

    return binary_tree
