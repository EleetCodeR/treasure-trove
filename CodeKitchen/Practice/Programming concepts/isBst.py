INT_MAX = 4294967296
INT_MIN = -4294967296


def check_BST_helper(node, mini, maxi):
    if node is None:
        return True

    if node.data < mini or node.data > maxi:
        return False

    return (check_BST_helper(node.left, mini, node.data - 1) and
            check_BST_helper(node.right, node.data+1, maxi))


def check_binary_search_tree_(root):
    return (check_BST_helper(root, INT_MIN, INT_MAX))
