'''
Given a string s consisting of only '0's and '1's,  find the last index of the '1' present.

Input: s = 00001
Output: 4'''

class Solution:
    def lastIndex(self, s):
        n=len(s)
        
        for i in range(n-1, -1, -1):
            if s[i]=='1':
                return i
        return -1
sol=Solution()
s='00001'
print(sol.lastIndex(s))