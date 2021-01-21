# Minimum number of coins to make change
# Difficulty: Medium

# Instruction:

#   Given an array of positive integers representing coin denominations and a
#   single non-negative integer n  representing a target amount of
#   money, write a function that returns the smallest number of coins needed to
#   make change for (to sum up to) that target amount using the given coin
#   denominations.

# Solution:
def minNumberOfCoinsForChange(n, denoms):
	minCoins = [float('inf') for amount in range(n + 1)]
	minCoins[0] = 0
	for denom in denoms:
		for amount in range(len(minCoins)):
			if denom <= amount:
				minCoins[amount] = min(minCoins[amount], minCoins[amount - denom] + 1)
	return minCoins[n] if minCoins[n] != float('inf') else  -1






    