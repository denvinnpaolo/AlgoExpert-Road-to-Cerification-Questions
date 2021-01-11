# Palindrome Check
# Difficulty: Easy

# Instruction:

#   Write a function that takes in a non-empty string and that returns a boolean
#   representing whether the string is a palindrome.

#   A palindrome is defined as a string that's written the same forward and
#   backward. Note that single-character strings are palindromes.

# Solution

def isPalindrome(string):
    # Write your code here.
	ans = True
    for i in range(len(string)):
		if string[i] == string[len(string) - i - 1]:
			continue
		else:
			ans = False
			
	return ans