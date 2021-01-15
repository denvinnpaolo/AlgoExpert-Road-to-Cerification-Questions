# Invert Binary Trees
# Difficulty: Medium

# Solution1:
def invertBinaryTree(tree):
    # Write your code here.
	queue = [tree]
	
	while queue:
		cur = queue.pop()
		
		if cur is None:
			continue
		cur.left, cur.right = cur.right, cur.left
		
		queue.append(cur.left)
		queue.append(cur.right)
		
		
# Solution 2:

def invertBinaryTree(tree):
    # Write your code here.
	if tree is not None:
		tree.left, tree.right = tree.right, tree.left
		invertBinaryTree(tree.left)
		invertBinaryTree(tree.right)


# This is the class of the input binary tree.
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None