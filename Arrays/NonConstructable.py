# Non-Constructable Change
# Easy
# Array

# Solution:
def nonConstructibleChange(coins):
    # Write your code here.
	
#Understand:
# given an array of positive integers representing values of coins
# goal: write a function that returns the minimum sum of money that you cannot 
# 	create with the coins in your possession 

# Plan:
# Sort the array to have a better perspective of the lowest number to highest
# for loop to go through the coins
	
	coins.sort()
	change = 0
	
	for coin in coins:
		if change + 1 < coin:
			return change + 1
		change += coin
			
	return change+1