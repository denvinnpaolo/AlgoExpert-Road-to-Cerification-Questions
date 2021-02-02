# Branch Sums
# Difficulty: Easy
# Type: Binary Tree

# Solution 

# This is the class of the input root. Do not edit it.
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def branchSums(root):
    # Write your code here.
	# sums will keep all sums for each leaf node 	
    sums = []
	
	#Push root as first node, sums to keep all sums, and running sum to add ancestor values plus current number	
	return branchSumsHelper(root, sums, 0)

def branchSumsHelper(node, sums, runningSum):
	#base case to see if theres a node 	
	if node == None:
		return sums
	
	#running sum is the sum where the ancestor values and the current node value will be added
	# this variable will be different each different path is takes 	
	runningSum += node.value
	
	# base case for when this function hits a left node 	
	if node.left is None and node.right is None:
		sums.append(runningSum)
	
	branchSumsHelper(node.left, sums, runningSum)
	branchSumsHelper(node.right, sums, runningSum)
	
	return sums