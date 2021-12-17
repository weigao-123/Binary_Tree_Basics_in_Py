"""
Basic binary tree introduction with some common problems.
Source: http://cslibrary.stanford.edu/110/BinaryTrees.html#csoln
"""

class TreeNode():
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def lookup(root, target):
    """
    Given a binary tree, return true if a node
    with the target data is found in the tree. Recurs
    down the tree, chooses the left or right
    branch by comparing the target to each node.
    
    """
    if not root:
        return False
    else:
        if root.val == target:
            return True
        else:
            # For any plain binary tree
            #return lookup(root.left, target) or lookup(root.right, target)
            # For binary search tree
            if root.val > target:
                return lookup(root.left, target)
            else:
                return lookup(root.right, target)

def insert(root, val):
    """
    Give a binary search tree and a number, inserts a new node
    with the given number in the correct place in the tree.
    Returns the new root pointer which the caller should
    then use (the standard trick to avoid using reference
    parameters).
    
    """
    if not root:
        return TreeNode(val)
    else:
        if root.val >= val:
            root.left = insert(root.left, val)
        else:
            root.right = insert(root.right, val)
        return root

def size(root):
    """
    Compute the number of nodes in a tree.
    
    """
    if not root:
        return 0
    return size(root.left) + size(root.right) + 1

def maxDepth(root):
    """
    Compute the "maxDepth" of a tree -- the number of nodes along
    the longest path from the root node down to the farthest leaf node.
    
    """
    if not root:
        return 0
    return max(maxDepth(root.left), maxDepth(root.right)) + 1

def minValue(root):
    """
    Given a non-empty binary search tree,
    return the minimum data value found in that tree.
    Note that the entire tree does not need to be searched.
    
    """
    if not root:
        return float('inf')
    else:
        # For any plain binary tree
        #return min(root.val, minValue(root.left), minValue(root.right))
        # For binary search tree
        return min(root.val, minValue(root.left))
    
def printTree(root):
    """
    Given a binary search tree, print out
    its data elements in increasing
    sorted order.
    
    """
    if not root:
        return
    printTree(root.left)
    print(root.val, end=' ')
    printTree(root.right)
    
def printPostorder(root):
    """
    Given a binary tree, print its
    nodes according to the "bottom-up"
    postorder traversal.
    
    """
    if not root:
        return
    printPostorder(root.left)
    printPostorder(root.right)
    print(root.val, end=' ')
    
def hasPathSum(root, target):
    """
    Given a tree and a sum, return true if there is a path from the root
    down to a leaf, such that adding up all the values along the path
    equals the given sum.
    Strategy: subtract the node value from the sum when recurring down,
    and check to see if the sum is 0 when you run out of tree.
    
    """
    if not root:
        return False
    elif not root.left and not root.right:
        return root.val == targetSum
    else:
        remain = targetSum - root.val
        return self.hasPathSum(root.left, remain) or self.hasPathSum(root.right, remain)
    
def printPaths(root):
    """
    Given a binary tree, print out all of its root-to-leaf
    paths, one per line. Uses a recursive helper to do the work.
    
    """
    paths = []
    def printPathsRecur(root, pathArr):
        """
        Recursive helper function -- given a node, and an array containing
        the path from the root node up to but not including this node,
        print out all the root-leaf paths.
        
        """
        if not root:
            return
        pathArr.append(root.val)
        if not root.left and not root.right:
            paths.append(pathArr.copy())     # important to avoid reference assignment
            print(pathArr)
        else:
            if root.left:
                printPathsRecur(root.left, pathArr)
                pathArr.pop()
            if root.right:
                printPathsRecur(root.right, pathArr)
                pathArr.pop()
        return paths
    paths = printPathsRecur(root, [])
    return paths

def mirror(root):
    """
     Change a tree so that the roles of the
     left and right pointers are swapped at every node.
     So the tree...
           4
          / \
         2   5
        / \
       1   3

     is changed to...
           4
          / \
         5   2
            / \
           3   1
    
    """
    if not root:
        return
    mirror(root.left)
    mirror(root.right)
    root.left, root.right = root.right, root.left
    
def doubleTree(root):
    """
    For each node in a binary search tree,
    create a new duplicate node, and insert
    the duplicate as the left child of the original node.
    The resulting tree should still be a binary search tree.
    So the tree...
        2
       / \
      1   3

    Is changed to...
           2
          / \
         2   3
        /   /
       1   3
      /
     1
    
    """
    if not root:
        return
    doubleTree(root.left)
    doubleTree(root.right)
    oldLeft = root.left
    root.left = TreeNode(root.val)
    root.left.left = oldLeft

def sameTree(roota, rootb):
    """
    Given two trees, return true if they are
    structurally identical.
    
    """
    if not roota and not rootb:
        return True
    if roota and rootb:
        return roota.val == rootb.val and sameTree(roota.left, rootb.left) and sameTree(roota.right, rootb.right)
    else:
        return False

def countTrees(numKeys):
    """
    For the key values 1...numKeys, how many structurally unique
    binary search trees are possible that store those keys.
    Strategy: consider that each value could be the root.
    Recursively find the size of the left and right subtrees.
    
    """
    if numKeys <= 1:
        return 1
    sum = 0
    # there will be one value at the root, with whatever remains
    # on the left and right each forming their own subtrees.
    # Iterate through all the values that could be the root...
    for root in range(1, numKeys+1):
        left = countTrees(root - 1)
        right = countTrees(numKeys - root)
        sum += left * right
    return sum

def isBST1(root):
    """
    Returns true if a binary tree is a binary search tree.
    
    """
    def minV(root):
        if not root:
            return float('inf')
        return min(root.val, minV(root.left), minV(root.right))
    def maxV(root):
        if not root:
            return float('-inf')
        return max(root.val, maxV(root.left), maxV(root.right)) 
    
    if not root:
        return True
    return maxV(root.left) <= root.val < minV(root.right) and isBST1(root.left) and isBST1(root.right)
    
def isBST2(root):
    """
    Returns true if the given tree is a binary search tree
    (efficient version).
    
    """
    def _isBST2(root, minVal, maxVal):
        if not root:
            return True
        return minVal <= root.val <= maxVal and _isBST2(root.left, minVal, root.val) and _isBST2(root.right, root.val+1, maxVal)
    return _isBST2(root, float('-inf'), float('inf'))
