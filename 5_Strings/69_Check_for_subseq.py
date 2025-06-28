'''
Given two strings A and B, find if A is a subsequence of B.

Input:
A = AXY 
B = YADXCP
Output: 0 '''

class Solution:
    def isSubSequence(self, A, B):
        it=iter(B)
        for char in A:
            if char not in it:
                return 0
        return 1
    
sol=Solution()
A = "AXY " 
B = "YADXCP" 
print(sol.isSubSequence(A, B))
