"""

Python code to sort string character in ascending order

"""

#taking input from the user
string = input("Enter the string : ")
#converting string into list of its characters
strList=list(string) 
#sorting elements of list
sortedString=''.join(sorted(strList)) 
print("String Sorted in ascending order :", sortedString)


"""
Python program to sort string in descending order

"""

#taking input from the user
string = input("Enter the string : ")
#converting string into list of its characters
strList=list(string) 
#sorting elements of list in reverse order by making ‘reverse = True’
sortedString=''.join(sorted(strList, reverse =True)) 
print("String Sorted in ascending order :", sortedString)