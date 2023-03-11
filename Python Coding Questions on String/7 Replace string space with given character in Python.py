#taking input from the user
string = input("Enter a String : ")
result = ''  #empty string
ch = input("Enter a Character : ")
for i in string:  #iterating using for loop
        if i == ' ':  #if any space found in the string
            i = ch   #replacing space with character
        result += i   #concatenating each character of the string without space
print('String after removing space with t = ',result)




string = "Once in a blue moon";  
ch = '-';  
   
#Replace space with specific character ch  
string = string.replace(' ', ch);  
   
print("String after replacing spaces with given character: ");  
print(string);  