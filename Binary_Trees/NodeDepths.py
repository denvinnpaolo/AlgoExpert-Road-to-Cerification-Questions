# Node Depths
# Difficulty: Easy
# Type: Binary Tree

# Solution:

def nodeDepths(root):
    depths = 0

    return nodeDepthsHelper(root, depths)

def nodeDepthsHelper(node, depths):
    if node is None:
        return 0
    
    return depths + nodeDepthsHelper(node.left, depths + 1) + nodeDepthsHelper(node.right, depths + 1)

class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None