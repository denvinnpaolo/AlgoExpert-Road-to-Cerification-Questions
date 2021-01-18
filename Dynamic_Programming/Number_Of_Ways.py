# Number of ways to make change
# Difficutly: Medium

# Instruction:

#   Given an array of distinct positive integers representing coin denominations and a
#   single non-negative integer n  representing a target amount of
#   money, write a function that returns the number of ways to make change for
#   that target amount using the given coin denominations.

# Solution:
def numberOfWaysToMakeChange(n, denoms):
    # Write your code here.
	if n == 0:
		return 1
	if len(denoms) == 1:
		if n % denoms[0] == 0:
			return 1
		else:
			return 0
	ans = 0
	d= {}
	a= []
	multiplier = 1
	
	for i in range(len(denoms)):
		while denoms[i] * multiplier <= n:
			num = denoms[i] * multiplier
			d[num] = num
			if num not in a:
				a.append(num)
				
			multiplier += 1
		multiplier = 1

	for i in range(len(denoms)):
		while denoms[i] * multiplier <= n:
			num = n - denoms[i] * multiplier 
			multiplier += 1
			if num in d:
				ans += 1
				
		multiplier = 1


    # if n == 0:
	# 	return 1
	
	# if len(denoms) == 1:
	# 	if n % denoms[0] == 0:
	# 		return 1
	# 	else: return 0
	
	
	
	# ans = 0
	# for i in range(len(denoms)):
	# 	if n % denoms[i] == 0:
	# 		ans += 1
	# 		print(ans)
	# 	else:
	# 		numNeeded = n % denoms[i]
	# 		print(numNeeded)
	# 		if numNeeded in denoms:
	# 			ans += 1
	# 		elif denoms[0] == 1:
	# 			ans += 1

	# return ans