# Number of ways to make change
# Difficutly: Medium

# Solution:
def numberOfWaysToMakeChange(n, denoms):
    # Write your code here.
    if n == 0:
		return 1
	
	if len(denoms) == 1:
		if n % denoms[0] == 0:
			return 1
		else: return 0
	
	
	
	ans = 0
	for i in range(len(denoms)):
		if n % denoms[i] == 0:
			ans += 1
			print(ans)
		else:
			numNeeded = n % denoms[i]
			print(numNeeded)
			if numNeeded in denoms:
				ans += 1
			elif denoms[0] == 1:
				ans += 1

	return ans