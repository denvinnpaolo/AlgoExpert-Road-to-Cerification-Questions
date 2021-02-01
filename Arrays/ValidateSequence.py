# Validate Subsequence
# Difficulty: Easy
# Type: Arrays

# Solution:

def isSubSeq(array, sequence):

#   array and sequence counter for iteration
    arr_c = 0
    seq_c = 0

    if len(array) < len(seqence):
        return False

    while seq_c < len(sequence):
        # Check if the current sequence value is in the array
        if seqence[seq_c] in array:
            # find the index of the current sequence value in the array then that will be the new array counter 
            # plus one so array counter can start after the current value we are searching for
            arr_c = array.index(sequence[seq_c]) + 1
            # manuipulate array so searching can only be done after the current value that was found
            array = array[arr_c:]
            # change the current sequence value
            seq_c += 1
        else: False
