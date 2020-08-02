'''
Check whether a given term represents a binary tree
    Write a predicate istree which returns true if and only if its argument is a list representing a binary tree.
    Example:
    * (istree (a (b nil nil) nil))
    T
    * (istree (a (b nil nil)))
    NIL
'''


def isTree(tree):
    if len(tree) != 3:  # checking if subtree or tree contains all root ,left and right nodes or not
        return False  # if not then it is nit a binary tree
    for node in tree:
        if isinstance(node, list):  # checking further nodes present or not
            if not isTree(node):  # then recursive calling with subtree
                return False

    return True


# declaring two trees in a form of list nested list represents subtree
tree_1 = ['a', ['b', None, None]]
tree_2 = ['a', ['b', None, None], None]

print(isTree(tree_1))
print(isTree(tree_2))
