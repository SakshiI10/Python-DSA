'''
You are given an array Arr of size N. Find the sum of distinct elements in an array.

Input:
N = 5
Arr[] = {1, 2, 3, 4, 5}
Output: 15
'''

class Solution:
    def findSum(self, arr, n):
        unique_num = set(arr)
        return sum(unique_num)

sol = Solution()
N = 5
Arr = [5, 5, 5, 5, 5]
print(sol.findSum(Arr, N))  # Output: 5

