# ThreeNumSum
# Difficulty: Easy

# Instruction:

#   Write a function that takes in a non-empty array of distinct integers and an
#   integer representing a target sum. The function should find all triplets in
#   the array that sum up to the target sum and return a two-dimensional array of
#   all these triplets. The numbers in each triplet should be ordered in ascending
#   order, and the triplets themselves should be ordered in ascending order with
#   respect to the numbers they hold.

#   If no three numbers sum up to the target sum, the function should return an
#   empty array.

# Solution 1:
def threeNumberSum(array, targetSum):
    # Write your code here.
	array.sort()
	ans = []
	
	for i in range(len(array)):
		left = i + 1
		right = len(array) - 1
		while left < right:
			curSum = array[i] + array[left] + array[right]
			
			if curSum == targetSum:
				ans.append([array[i], array[left], array[right]])
				left += 1
				right -= 1
			elif curSum < targetSum:
				left += 1
			elif curSum > targetSum:
				right -= 1
				
	return ans


# Solution 2:
	ans = []
	d ={}
	
	for i in range(len(array)):
		for j in range(len(array)):
			if i == j:
				continue
			
			num = targetSum - (array[i] + array[j])
			
			if num in d:
				d[num].append([array[i], array[j]])
			else:
				d[num] = [[array[i], array[j]]]
				
	for i in range(len(array)):
		if array[i] in d:
			for j in range(len(d[array[i]])):
				if array[i] in d[array[i]][j]:
					continue
				
				possible_ans = d[array[i]][j][0] + d[array[i]][j][1] + array[i]
				
				if possible_ans == targetSum:
					d[array[i]][j].append(array[i])

					d[array[i]][j].sort()
					if d[array[i]][j] not in ans:
						ans.append(d[array[i]][j])
	ans.sort()
	return ans
