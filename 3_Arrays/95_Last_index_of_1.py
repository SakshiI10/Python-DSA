'''
Given a string s consisting of only '0's and '1's,  find the last index of the '1' present.

Input: s = 00001
Output: 4'''

class Solution:
    def firstIndex(self, arr):
        n=len(arr)
        for i in range(n):
            if arr[i]==1:
                return i
        return -1
    
    def lastIndex(self, s):
        n=len(s)
        
        for i in range(n-1, -1, -1):
            if s[i]=='1':
                return i
        return -1
    
sol=Solution()
arr=[0, 0, 0, 0, 0, 0, 1, 1, 1, 1]
s='00001'
print(sol.firstIndex(arr))
print(sol.lastIndex(s))
