
"""
Using replace() method
"""

def remove_char(s1,s2):
    print(s1.replace(s2, ''))
s1 = input("please give a String : ")
s2 = input("please give a Character to remove : ")
remove_char(s1,s2) 

"""
using translate() method
"""

def remove_char(s1,s2):
    dict = {ord(s2) : None}
    print(s1.translate(dict))
s1 = input("please give a String : ")
s2 = input("please give a Character to remove : ")
remove_char(s1,s2) 