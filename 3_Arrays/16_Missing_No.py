'''
Given an array A of size N. The contents of A are copied into another array B and numbers are shuffled. Also, one element is removed from B. The task is to find the missing element.

Input : 
A[] = {4, 8, 1, 3, 7}
B[] = {7, 4, 3, 1}
Output : 8'''

class Solution:
    def findMissing(self, a, b, n):
        a.sort()
        b.sort()
        
        for i in range(n-1):
            if a[i] != b[i]:
                return a[i]
        return a[-1]

sol = Solution()
A = [4, 8, 1, 3, 7]
B = [7, 4, 3, 1]
N = len(A)
output = sol.findMissing(A, B, N)
print(output)  # Output: 8
