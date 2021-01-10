# Node Depths
# Difficulty: Easy

# Instruction:
#   The distance between a node in a Binary Tree and the tree's root is called the
#   node's depth.
#
#   Write a function that takes in a Binary Tree and returns the sum of its nodes'
#   depths.
# 
#   Each "BinaryTree" node has an integer "value", a "left" child node, and a "right" child node. 
#   Children nodes can either be "BinaryTree" nodes themseleves or "None/null"


# Solution 1:

def nodeDepths(root, depth = 0):
	if root is None:
		return 0
	
	return depth + nodeDepths(root.left, depth + 1) + nodeDepths(root.right, depth + 1)


# This is the class of the input binary tree.
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


# Solution 2:

# def nodeDepths(root):
#     # Write your code here.
# 	stack = []
# 	stack.append(root)
# 	depthsTotal = 0
# 	cur_dep = 0
	
# 	while stack != None:
# 		node = stack.pop()
		
# 		if node.right:
# 			stack.append(node.right)
		
# 		if node.left:
# 			stack.append(node.left)
		
		
# # This is the class of the input binary tree.
# class BinaryTree:
#     def __init__(self, value):
#         self.value = value
#         self.left = None
#         self.right = None



{
  "tree": {
    "nodes": [
      {"id": "1", "left": "2", "right": "3", "value": 1},
      {"id": "2", "left": "4", "right": "5", "value": 2},
      {"id": "3", "left": "6", "right": "7", "value": 3},
      {"id": "4", "left": "8", "right": "9", "value": 4},
      {"id": "5", "left": null, "right": null, "value": 5},
      {"id": "6", "left": "10", "right": null, "value": 6},
      {"id": "7", "left": null, "right": null, "value": 7},
      {"id": "8", "left": null, "right": null, "value": 8},
      {"id": "9", "left": null, "right": null, "value": 9},
      {"id": "10", "left": null, "right": "11", "value": 10},
      {"id": "11", "left": "12", "right": "13", "value": 11},
      {"id": "12", "left": "14", "right": null, "value": 12},
      {"id": "13", "left": "15", "right": "16", "value": 13},
      {"id": "14", "left": null, "right": null, "value": 14},
      {"id": "15", "left": null, "right": null, "value": 15},
      {"id": "16", "left": null, "right": null, "value": 16}
    ],
    "root": "1"
  }
}