'''
Given string s that is appended with a number at last. The task is to check whether the length of string excluding that number is equal to that number.

Input:  s = "geeks5"
Output: 1'''

class Solution:
    def isSame(self, s):
        number = ''
        text = ''
        
        for char in s:
            if char.isdigit():
                number += char  
            else:
                text += char      

        if len(text) == int(number):
            return 1
        else:
            return 0

sol=Solution()
s="geeks5"
print(sol.isSame(s))
