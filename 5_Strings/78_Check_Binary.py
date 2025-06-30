'''
Given a non-empty sequence of characters s, return true if sequence is Binary, else return false.

Input: s = "101"
Output: true'''

class Solution:
    def isBinary(self, s):
        cnt = 0
        for i in str:
            if i == '0' or i == '1':
                cnt += 1
        if cnt == len(str):
            return True
        return False
        
sol=Solution()
s = "102"
print(sol.isBinary(s))