# Levenshtein Distance
# Difficulty: Medium

# 

# Solution
def levenshteinDistance(str1, str2):
    # Write your code here.
	matrix = [[x for x in range(len(str1) + 1)] for y in range(len(str2) + 1)]
	
	for i in range(1, len(str2) + 1):
		matrix[i][0] = matrix[i - 1][0] + 1
		
	for i in range(1, len(str2) + 1):
		for j in range(1, len(str1) + 1):
			if str2[i - 1] == str1[j - 1]:
				matrix[i][j] = matrix[i - 1][j - 1]
				
			else:
				matrix[i][j] = 1 + min(matrix[i-1][j], matrix[i][j-1], matrix[i-1][j-1])
		
	return matrix[-1][-1]