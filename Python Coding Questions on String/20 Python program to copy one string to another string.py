## Iterative Python Program to copy one String
# to another.
# Function to copy one string to other
def myCopy(s1,s2):
	# traversing the string s1 from start to end
	for i in range(len(s1)):
		# copying value one by one
		s2[i]=s1[i]
	return "".join(s2)

#Driver code
s1=list("GEEKSFORGEEKS")
s2=[""]*len(s1)
print(myCopy(s1,s2))
