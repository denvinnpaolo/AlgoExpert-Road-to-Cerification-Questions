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

def findClosestValueInBst(tree, target):
    # Write your code here.
	# cur is the current node to be checked 	
	cur = tree
	# closest initial value will be the very first value 	
	closest = cur.value
	
	# this while loop is going to execute until it hits a "None" 	
	while cur is not None:
		#if statement to check if the current node value minus target is
		#less than current closest number to the target		
		if abs(cur.value - target) < abs(closest - target):
			closest = cur.value
	 		
		if target < cur.value:
			cur = cur.left
		elif target > cur.value:
			cur = cur.right
		else:
			break

	return closest

# This is the class of the input tree. Do not edit.
class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
