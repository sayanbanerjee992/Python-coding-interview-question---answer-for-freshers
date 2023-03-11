# checking for digit
string = '15460'
print(string.isdigit())

string = '154ayush60'
print(string.isdigit())







newstring =''

# Initialising the counters to 0
count = 0

# Incrementing the counter if a digit is found
# and adding the digit to a new string
# Finally printing the count and the new string

for a in range(53):
	b = chr(a)
	if b.isdigit() == True:
		count+= 1
		newstring+= b
		
print("Total digits in range :", count)
print("Digits :", newstring)





#taking input from user
ch = input("Enter a character : ") 
if ch >= '0' and ch <= '9': #comparing the value of ‘ch’ 
	# if the condition holds true then this block will execute
    	print("Given Character ", ch, "is a Digit")
else: #this block will execute if the condition will not satisfies
    print("Given Character ", ch, "is not a Digit")

