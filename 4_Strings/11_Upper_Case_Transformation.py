'''
Given a string str, convert the first letter of each word in the string to uppercase. 

Input:
str = "i love programming"
Output: "I Love Programming"'''

class Solution:
    def to_upper(self, str):
        return str.title()
            
sol=Solution()
str = "i love programming"
print(sol.to_upper(str))
 