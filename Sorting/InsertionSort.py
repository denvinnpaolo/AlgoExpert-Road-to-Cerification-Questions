# Insertion Sort
# Difficulty: Easy

# Instruction:

#   Write a function that takes in an array of integers and returns a sorted
#   version of that array. Use the Insertion Sort algorithm to sort the array.

#   If you're unfamiliar with Insertion Sort, we recommend watching the Conceptual
#   Overview section of this question's video explanation before starting to code.

# Solution:
def insertionSort(array):
    # Write your code here.
	for i in range(1, len(array)):
		cur = i
		sorted_counter = i - 1
		
		while array[sorted_counter] > array[cur]:
			array[sorted_counter], array[cur] = array[cur], array[sorted_counter]
			
			if sorted_counter == 0:
				continue
				
			sorted_counter -= 1
			cur -=1
			
	return array