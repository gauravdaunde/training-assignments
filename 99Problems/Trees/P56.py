'''
Symmetric binary trees
    Let us call a binary tree symmetric if you can draw a vertical line 
    through the root node and then the right subtree is the mirror image
     of the left subtree. Write a predicate symmetric/1 to check whether 
     a given binary tree is symmetric. Hint: Write a predicate mirror/2 
     first to check whether one tree is the mirror image of another. We 
     are only interested in the structure, not in the contents of the nodes.
'''

from P57 import createTree, BinaryTree


def getTreeInList(tree_obj):
    # traversing through tree and generating a list dfs
    li = list([tree_obj.data])
    if isinstance(tree_obj.left, BinaryTree):
        li.append(getTreeInList(tree_obj.left))
    else:
        li.append(tree_obj.left)

    if isinstance(tree_obj.right, BinaryTree):
        li.append(getTreeInList(tree_obj.right))
    else:
        li.append(tree_obj.right)

    return li


def compare(left_tree, right_tree):
    # checking for similar tree structure
    for i in range(len(left_tree)):
        if type(left_tree[i]) == type(right_tree[i]):
            if isinstance(left_tree[i], list) and isinstance(right_tree[i], list):
                return compare(left_tree[i], right_tree[i])
        else:
            return False
    return True


def isSymmetric(tree):
    tree_list = getTreeInList(tree)
    print(tree_list)
    return compare(tree_list[1], tree_list[-1])


nodes_list = [5, 3, 18, 1, 4, 12, 21]
binary_tree = createTree(nodes_list)

print(isSymmetric(binary_tree))
