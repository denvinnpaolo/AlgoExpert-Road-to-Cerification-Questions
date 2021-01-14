# Binary Search Tree Traversal
# Difficulty: Medium

# Solution:

def inOrderTraverse(tree, array):
    # Write your code here.
	if tree is not None:
		inOrderTraverse(tree.left, array)
		array.append(tree.value)
		inOrderTraverse(tree.right, array)

	return array

def preOrderTraverse(tree, array):
    # Write your code here.
    if tree is not None:
		array.append(tree.value)
		preOrderTraverse(tree.left, array)
		preOrderTraverse(tree.right, array)

	return array