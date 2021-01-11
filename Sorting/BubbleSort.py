# Bubble Sort
# Difficulty: Easy

# Instruction:

#   Write a function that takes in an array of integers and returns a sorted
#   version of that array. Use the Bubble Sort algorithm to sort the array.

#   If you're unfamiliar with Bubble Sort, we recommend watching the Conceptual
#   Overview section of this question's video explanation before starting to code.

# Solution 1:

def bubbleSort(array):
	sorting = False
	
	while not sorting:
		sorting = True
		for i in range(len(array) - 1):
			if array[i] > array[i + 1]:
				array[i], array[i + 1] = array[i + 1], array[i]
				sorting = False
		
				
	return array