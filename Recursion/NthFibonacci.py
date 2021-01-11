# Nth Fibonacci 
# Difficulty: Easy

# Instruction:
# 
#   The Fibonacci sequence is defined as follows: the first number of the sequence
#   is 0 , the second number is 1 , and the nth number is the sum of the (n - 1)th
#   and (n - 2)th numbers. Write a function that takes in an integer "n"  
#   and returns the nth Fibonacci number.

# Solution 1: Recurision
def getNthFib(n):
    # Write your code here.
	
	if n == 1:
		return 0
	
	if n == 2:
		return 1
	
	return getNthFib(n-1) + getNthFib(n-2)


# Solution 2: Memoize
    def getNthFib(n):
    # Write your code here.
	d = {
		1 : 0,
		2 : 1
	}

	if n in d:
		return d[n]
	else:
		for i in range(3, n+1):
			d[i] = d[i - 1] + d[i - 2]
			
		return d[n]
  