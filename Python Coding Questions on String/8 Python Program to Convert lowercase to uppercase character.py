string = input("Enter a String : ")
result=''
for i in string:  #iterate through each letter/character from the string
        if i.islower():  #if lowercase
            i = i.upper() #converting lowercase into uppercase letter
        result += i #concatenating each character of the string without lowercase letter 
print("String after converting lower case to upper :",result)








# Python3 program to implement
# the above approach

# Function to convert vowels
# into uppercase
def conVowUpp(str):
	
	# Stores the length
	# of str
	N = len(str)
	
	str1 =""
	
	for i in range(N):
		if (str[i] == 'a' or str[i] == 'e' or
			str[i] == 'i' or str[i] == 'o' or
			str[i] == 'u'):
			c = (str[i]).upper()
			str1 += c
		else:
			str1 += str[i]

	print(str1)

# Driver Code
if __name__ == '__main__':
	
	str = "eutopia"
	
	conVowUpp(str)


