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