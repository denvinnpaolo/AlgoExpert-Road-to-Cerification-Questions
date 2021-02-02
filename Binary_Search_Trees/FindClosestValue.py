# Find Closest Value in BST
# Difficulty: Easy
# Type: BST

# Solution (Recursion):
def findClosestValueInBst(tree, target):
    # Write your code here.	
	return closestValueHelper(tree, target, tree.value)

def closestValueHelper(tree, target, closest):
	if tree is None: return closest
	
	if abs(tree.value - target) < abs(closest - target):
		closest = tree.value
		
	if target < tree.value:
		return closestValueHelper(tree.left, target, closest)
	elif target > tree.value:
		return closestValueHelper(tree.right, target, closest)
	else:
		return closest

	
# Solution (Iteration):

# This is the class of the input tree. Do not edit.
class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
