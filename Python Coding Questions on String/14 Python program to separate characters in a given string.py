string = "characters";  
#Displays individual characters from given string  
print("Individual characters from given string:");  
#Iterate through the string and display individual character  
for i in range(0, len(string)):  
    print(string[i], end="  ");  
    
    
    
string = "geeks"
print([*string])



string = 'geeksforgeeks'
lst = []
for letter in string:
	lst.append(letter)
print(lst)



string = "Geeksforgeeks"
letter = [x for x in string]
print(letter)




def split(word):
	return list(word)
# Driver code
word = 'geeks'
print(split(word))



