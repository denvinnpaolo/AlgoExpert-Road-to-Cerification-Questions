# Caesar Cipher Encryptor
# Diffitculty: Easy

# Instruction:

#   Given a non-empty string of lowercase letters and a non-negative integer
#   representing a key, write a function that returns a new string obtained by
#   shifting every letter in the input string by k positions in the alphabet,
#   where k is the key.


#   Note that letters should "wrap" around the alphabet; in other words, the
#   letter "z"  shifted by one returns the letter "a"

# Solution 1:

def caesarCipherEncryptor(string, key):
    # Write your code here.
    ans=''
        for i in range(len(string)):
            new_letter = ord(string[i]) + key % 26
            if new_letter > 122:
                new_letter = new_letter - 26
            
            ans+= chr(new_letter)
        
        return ans

# Solution 2:
	for i in range(len(string)):
		char = ord(string[i])
		if key > 26:
			key = key % 26
			
		if key + char > 122:
			char = chr((char + key - 122) + 96)
			ans += char
		else:
			char += key
			ans += chr(char)
			
	
	return ans