# Find Three Largest
# Difficulty: Easy

# Instruction:

#   Write a function that takes in an array of at least three integers and,
#   without sorting the input array, returns a sorted array of the three largest
#   integers in the input array.

#   The function should return duplicate integers if necessary; for example, it
#   should return [10, 10, 12]  for an input array of [10, 5, 9, 10, 12]

def findThreeLargestNumbers(array):

# Solution 1:
    # Write your code here.
    first = -999
	second = -999
	third = -999
	
	for num in array:
		if num >= third:
			first = second
			second = third
			third = num

		elif num < third:
			if num >= second:
				first = second
				second = num
			elif num < second:
				if num >= first:
					first = num
					
	return [first, second, third]

# Solution 2

    largest = [-9999,-9999,-9999]
	
	for num in array:
		if num > largest[2]:
			old_largest = largest[2]
			mid_largest = largest[1]
			
			largest[2] = num
			largest[1] = old_largest
			largest[0] = mid_largest
		elif num <= largest[2] and num > largest[1]:
			mid_largest = largest[1]
			
			largest[1] = num
			largest[0] = mid_largest 
		elif num <= largest[1] and num >= largest[0]:
			
			largest[0] = num
		else:
			continue
			
			
			
	
	return largest