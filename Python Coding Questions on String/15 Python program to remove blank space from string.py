#taking input from the user
string = input("Enter a String : ")
result=''
#iterating the string
for i in string:
    #if the character is not a space
    if i!=' ':
        result += i
print("String after removing the spaces :",result)






# Python3 code to remove whitespace
def remove(string):
    return string.replace(" ", "")
     
# Driver Program
string = ' g e e k '
print(remove(string))



# Python3 code to remove whitespace
def remove(string):
    return "".join(string.split())
     
# Driver Program
string = ' g e e k '
print(remove(string))


# Python3 code to remove whitespace
import re

def remove(string):
	pattern = re.compile(r'\s+')
	return re.sub(pattern, '', string)
	
# Driver Program
string = ' g e e k '
print(remove(string))





