''' 
Given a string s. The task is to convert characters of string to lowercase.

Input: 
s = "ABCddE"
Output: "abcdde"'''

class Solution:
    def toLower (self , s : str)-> str :
        return s.lower()
    
sol=Solution()
print(sol.toLower('ABCdEf')) 