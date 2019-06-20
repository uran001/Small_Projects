
from linked_binary_tree import LinkedBinaryTree

class Node:
    # Constructor to create a new binary node
    def __init__(self, key):
        self.key =  key
        self.left = None
        self.right = None

def build_UNIST_tree():
    """
    This function should return a binary tree that contains (a simplified and fictitious  version of) the organisational
    structure of schools and departments at UNIST. In particular, this function should return the following tree:
`+-*
    UNIST
    --Engineering
    ----Management Engineering
    ------Big data
    ------Business process management
    ----Materials Engineering
    ------Wood
    ------Plastic
    --Business
    ----Business Administration

    :return: the UNIST tree
    """
    UNIST = LinkedBinaryTree()
    root = UNIST._add_root("UNIST")
    EE = UNIST._add_left(root, "Engineering")
    BU = UNIST._add_right(root, "Bussiness")

    MNE = UNIST._add_left(EE, "Management Engineering")
    UNIST._add_left(MNE, "Big data")
    UNIST._add_right(MNE, "Business process management")
    MTE = UNIST._add_right(EE, "Material Engineering")
    UNIST._add_left(MTE,"Wood")
    UNIST._add_right(MTE, "Plastic")

    UNIST._add_left(BU, "Business Administration")

    return UNIST
def FindPath(root, path, k):
    if root is None:
        return False
    path.append(root.element)

    if root.element() == k:
        return True

    if ((root.left(root.element()) != None and FindPath(root.left(root.element()), path, k)) or (root.right(root.element()) != None and FindPath(root.right(root.element()), path, k))):
        return True

    path.pop()
    return False


def findPath(root, path, k):
    # Baes Case
    if root is None:
        return False

    # Store this node is path vector. The node will be
    # removed if not in path from root to k
    path.append(root.key)

    # See if the k is same as root's key
    if root.key == k:
        return True

    # Check if k is found in left or right sub-tree
    if ((root.left != None and findPath(root.left, path, k)) or
            (root.right != None and findPath(root.right, path, k))):
        return True

        # If not present in subtree rooted with root, remove
    # root from path and return False

    path.pop()
    return False


# Returns LCA if node n1 , n2 are present in the given
# binary tre otherwise return -1
def findLCA(root, n1, n2):
    # To store paths to n1 and n2 fromthe root
    path1 = []
    path2 = []

    # Find paths from root to n1 and root to n2.
    # If either n1 or n2 is not present , return -1
    if (not findPath(root, path1, n1) or not findPath(root, path2, n2)):
        return -1

        # Compare the paths to get the first different value
    i = 0
    while (i < len(path1) and i < len(path2)):
        if path1[i] != path2[i]:
            break
        i += 1
    return path1[i - 1]


def preorder_indent(T, p, d):

    print(2 * d * '-' + str(p.element()))
    for c in T.children(p):
        preorder_indent(T, c, d + 1)



if __name__ == '__main__':

    tree = build_UNIST_tree()

    # print the tree
    preorder_indent(tree,tree.root(),0)

    """ some code showing how to find positions in a binary tree, please check"""
    root = tree.root()                              # the root position of tree
    p_engineering = tree.left(root)                 # the left child position of the root position
    p_business = tree.right(root)                   # the right child position of the root position
    print(p_engineering.element())
    print(p_business.element())
    p_man_eng = tree.left(p_engineering)            # the left child position of the p_engineering position
    print(p_man_eng.element())

    """implement here the code to test the LCA function that you implemented """
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.left = Node(6)
    root.right.right = Node(7)
    print("LCA(4, 5) = {0}".format(findLCA(root, 4, 5)))
    print("LCA(4, 6) = {0}".format(findLCA(root, 4, 6)))
    print("LCA(3, 4) = {0}".format(findLCA(root, 3, 4)))
    print("LCA(2, 4) = {0}".format(findLCA(root, 2, 4)))