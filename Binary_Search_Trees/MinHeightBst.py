# Min Height Bst
# Difficulty: Medium

# Solution:

def minHeightBst(array):
	return minHeightBstHelper(array, 0, len(array) - 1)
    
def minHeightBstHelper(array, left, right):
	if right < left:
		return None
	mid = (left + right) // 2
	bst = BST(array[mid])
	bst.left = minHeightBstHelper(array, left, mid - 1)
	bst.right = minHeightBstHelper(array, mid + 1, right)

		
	return bst
    

class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        if value < self.value:
            if self.left is None:
                self.left = BST(value)
            else:
                self.left.insert(value)
        else:
            if self.right is None:
                self.right = BST(value)
            else:
                self.right.insert(value)
