'''
You are given a binary string s of length n. You have to perform binary addition of the string with '1'.

n = 4
s = 1010
Output: 1011'''

class Solution:
    def binaryAdd(self, n, s):
        res=bin(int(s, 2) + 1)[2:]
        return res.zfill(n)
    
sol=Solution()
n=4
s='1010'
print(sol.binaryAdd(n, s))
