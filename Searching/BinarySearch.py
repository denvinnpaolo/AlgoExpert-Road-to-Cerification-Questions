# Binary Search
# Difficulty: Easy

# Instruction:
# 
#   Write a function that takes in a sorted array of integers as well as a target
#   integer. The function should use the Binary Search algorithm to determine if
#   the target integer is contained in the array and should return its index if it
#   is, otherwise "-1" 


#   If you're unfamiliar with Binary Search, we recommend watching the Conceptual
#   Overview section of this question's video explanation before starting to code.


# SOLUTION:

def binarySearch(array, target):
    # Write your code here.

#UPER

# UNDERSTAND:
# Problem is giving a SORTED array and a target
# the midpoint value and compare to target
# if midpoint is lower, search the right side of the array
# if midpoint is higher, search the left side of the array
# then... get the midpoint of starting from the midpoint to whichever
# side the value is closer and repeat the process till you're down to your
# last number
# if the number is not the target return "-1"

# PLAN:
# 1.Recursion:
# 	-get midpoint
# 	-check if midpoint is lower or higher than target
# 	-push to binarySearch function with the closer part of the array
# 	-repeat till down to last number or found target

# 2.While Loop:
# 	-get midpoint
# 	-use a condition to stop the while looop
# 	-while value != target or array.length == 1

# EXECUTE:
	return binarySearchHelper(array, target, 0, len(array) - 1)

def binarySearchHelper(array, target, left, right):
	if left > right:
		return -1
	
	mid = (left + right) // 2
	
	if array[mid] == target:
		return mid
	elif array[mid] > target:
		return binarySearchHelper(array, target, left, mid - 1)
	elif array[mid] < target:
		return binarySearchHelper(array, target, mid + 1, right)
	
	