str1 = input('Enter a string: ')
sum=0
for i in str1:
	#if character is a digit
    if i.isdigit():
		#taking sum of integral digits present in the string 
        sum=sum+int(i)
print("sum=",sum)


