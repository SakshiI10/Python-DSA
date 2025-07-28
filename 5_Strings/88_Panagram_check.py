'''
Given a string s, check if it is a "Panagram" or not. Return true if the string is a Panagram, else return false.

A "Panagram" is a sentence containing every letter in the English Alphabet either in lowercase or Uppercase.

Input: s = "Bawds jog, flick quartz, vex nymph"
Output: true'''

class Solution:
    def checkPangram(self,s):
        s=s.lower()
        alpha_set=set('abcdefghijklmnopqrstuvwxyz')
        input_set=set(s)
        return alpha_set.issubset(input_set)
    
sol=Solution()
s = "Bawds jog, flick quartz, vex nymph"
print(sol.checkPangram(s))
