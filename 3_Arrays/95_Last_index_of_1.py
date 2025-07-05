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
        digits=list(str(s))
        n=len(digits)
        
        for i in range(n-1, -1, -1):
            if digits[i]=='1':
                return i
        return -1
    
sol=Solution()
arr=[0, 0, 0, 0, 0, 0, 1, 1, 1, 1]
print(sol.firstIndex(arr))

s='00001'
print(sol.lastIndex(s))
