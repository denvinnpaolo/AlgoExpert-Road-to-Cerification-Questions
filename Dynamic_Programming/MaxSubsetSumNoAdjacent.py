# Max Subset Sum No Adjacent
# Difficulty: Medium

# Instruction:

#   Write a function that takes in an array of positive integers and returns the
#   maximum sum of non-adjacent elements in the array.

#   If the input array is empty, the function should return 0

# Solution:

def maxSubsetSumNoAdjacent(array):
    # Write your code here.
	if len(array) == 0: 
		return 0
	elif len(array) == 1:
		return array[0]
	else:
		maxSums = [0] * (len(array))
		for i in range(len(array)):
			maxSums[i] = max(maxSums[i - 1], maxSums[i - 2] + array[i])
			print(maxSums[i - 2],  array[i])
			print(maxSums)
		
			
		return max(maxSums[len(array) - 1], maxSums[len(array)-2])
        # or
        return maxSums[-1]

				
