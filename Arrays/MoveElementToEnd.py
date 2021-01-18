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