# Validate BST
# Difficulty: Medium

# Instruction:


# Solution:
class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def validateBst(tree):
    # Write your code here.
    return validateBstHelper(tree, float('-inf'), float('inf'))

def validateBstHelper(tree, min_value, max_value):
	if tree is None:
		return True
	
	if tree.value < min_value or tree.value >= max_value:
		return False
	
	left_is_val = validateBstHelper(tree.left, min_value, tree.value)
	
	return left_is_val and validateBstHelper(tree.right, tree.value, max_value)
	
	
		
