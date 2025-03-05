'''
Given a string S, the task is to change the complete string to Uppercase or Lowercase depending upon the case for the first character.

Input: S = "abCD"
Output: abcd'''

def change_case(s):
    if s[0].islower():
        return s.lower() 
    else:
        return s.upper()  
    
s1 = "abCD"
print(change_case(s1))  # Output: abcd

s2 = "Abcd"
print(change_case(s2))  # Output: ABCD
