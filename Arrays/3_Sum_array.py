'''
Given an integer array arr[] of size n. The task is to find sum of it.

Input:
n = 4
arr[] = {1, 2, 3, 4}
Output: 10
Explanation: 1 + 2 + 3 + 4 = 10.'''

class Solution:
    def sum(self, arr, n):
        sum = 0
        for i in range(n):
            sum += arr[i]
        return sum
    
sol = Solution()
arr = [1, 2, 3, 4]
n = 4
print(sol.sum(arr, n))