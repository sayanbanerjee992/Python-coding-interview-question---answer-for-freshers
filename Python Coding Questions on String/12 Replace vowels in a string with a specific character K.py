# Function to Replace each vowel in
# the string with a specified character
def replaceVowelsWithK(test_str, K):

	# string of vowels
	vowels = 'AEIOUaeiou'

	# iterating to check vowels in string
	for ele in vowels:

		# replacing vowel with the specified character
		test_str = test_str.replace(ele, K)

	return test_str

# Driver Code
# input string
input_str = "Geeks for Geeks"
# specified character
K = "#"
# printing input
print("Given String:", input_str)
print("Given Specified Character:", K)
# printing output
print("After replacing vowels with the specified character:",
	replaceVowelsWithK(input_str, K))





# Function to Replace each vowel
# in the string with a specified character
def replaceVowelsWithK(test_str, K):

	# creating list of vowels
	vowels_list = ['A', 'E', 'I', 'O', 'U', 'a', 'e', 'i', 'o', 'u']

	# creating empty list
	new_string = []

	# converting the given string to list
	string_list = list(test_str)

	# running 1st iteration for
	# comparing all the
	# characters of string with
	# the vowel characters
	for char in string_list:

		# running 2nd iteration for
		# comparing all the characters
		# of vowels with the string character
		for char2 in vowels_list:

			# comparing string character
			# and vowel character
			if char == char2:

				# if condition is true then adding
				# the specific character entered
				# by the user in the new list
				new_string.append(K)
				break

		# else adding the character
		else:
			new_string.append(char)

	# return the converted list into string
	return(''.join(new_string))

# Driver Code
# input string
input_str = "Geeks for Geeks"
# specified character
K = "#"
# printing input
print("Given String:", input_str)
print("Given Specified Character:", K)
# printing output
print("After replacing vowels with the specified character:",
	replaceVowelsWithK(input_str, K))




# Function to Replace each vowel in
# the string with a specified character
import re
def replaceVowelsWithK(test_str, K):

	# string of vowels
	vowels = 'AEIOUaeiou'
	return re.sub(rf'[{vowels}]', K, test_str)

# Driver Code
# input string
input_str = "Geeks for Geeks"
# specified character
K = "&"
# printing input
print("Given String:", input_str)
print("Given Specified Character:", K)
# printing output
print("After replacing vowels with the specified character:",
	replaceVowelsWithK(input_str, K))




# Function to Replace each vowel
# in the string with a specified character
vowels = {
	"a": 0, "e": 0, "i": 0, "o": 0, "u": 0,
	"A": 0, "E": 0, "I": 0, "O": 0, "U": 0}


def replaceVowelsWithK(test_str, K):
	# creating empty list
	new_string = []

	# converting the given string to list
	string_list = list(test_str)

	# running 1st iteration for
	# comparing all the
	# characters of string with
	# the vowel characters
	for char in string_list:

		if char in vowels.keys():
			new_string.append(K)

		# else adding the character
		else:
			new_string.append(char)

	# return the converted list into string
	return(''.join(new_string))

# Driver Code
# input string
input_str = "Geeks for Geeks"
# specified character
K = "#"
# printing input
print("Given String:", input_str)
print("Given Specified Character:", K)
# printing output
print("After replacing vowels with the specified character:",
	replaceVowelsWithK(input_str, K))



# Program to Replace each vowel in
# the string with a specified character
# input string
input_str = "Geeks for Geeks"
# specified character
K = "#"
# printing input
print("Given String:", input_str)
print("Given Specified Character:", K)
vow=[97, 101, 105, 111, 117, 65, 69, 73, 79, 85]
for i in input_str:
	if ord(i) in vow:
		input_str=input_str.replace(i,K)
# printing output
print("After replacing vowels with the specified character:",input_str)
