''' 
Given a string s , return reverse of the string as output.

Input: 
s = "GeeksforGeeks"
Output: "skeeGrofskeeG" '''

class Solution:
    def revStr (self, s : str) -> str :
        return s[::-1]

sol = Solution()
str = "qwerty"
print(sol.revStr(str))

'''
Given two strings S1 and S2 as input. Your task is to concatenate two strings and then reverse the string. Finally print the reversed string.
Input: S1 = "Geeks" , S2 = "forGeeks"
Output: "skeeGrofskeeG" 
'''
class Solution:
    def conRevstr (ob, S1, S2):
        combined = S1 + S2
        rev_str=combined[::-1]
        return rev_str


sol = Solution()
S1= "Geeks"
S2= "forGeeks"  
print(sol.conRevstr(S1, S2))