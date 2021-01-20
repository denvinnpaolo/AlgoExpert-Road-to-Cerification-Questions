# Move Element To End
# Difficulty: Medium

# Solution:
def moveElementToEnd(array, toMove):
    # Write your code here.
	for i in range(len(array)):
		if array[i] == toMove:
			array.pop(i)
			array.append(toMove)

    for i in range(len(array)):
		if array[i] == toMove:
			array.pop(i)
			array.append(toMove)
    for i in range(len(array)):
		if array[i] == toMove:
			array.pop(i)
			array.append(toMove)

    return array

# Solution 2;
	if toMove not in array:return array
	
	for i in range(len(array)):
		if array[i] != toMove:
			index = array.index(toMove)
			array[i], array[index] = array[index], array[i]
	return array