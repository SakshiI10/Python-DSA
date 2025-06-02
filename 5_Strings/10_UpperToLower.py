''' 
Given a string s. The task is to convert characters of string to lowercase.

Input: 
s = "ABCddE"
Output: "abcdde"'''

class Solution:
    def toLower (self , s):
        return s.lower()
    
        # result = ''
        # for c in s:
        #     result += c.lower()
        # return result
    
        # return s.upper() //If asked for upper case transformation

sol=Solution()
print(sol.toLower('ABCdEf')) 