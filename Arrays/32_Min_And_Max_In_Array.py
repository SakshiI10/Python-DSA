'''
Given an array arr. Your task is to find the minimum and maximum elements in the array.

Input: arr = [3, 2, 1, 56, 10000, 167]
Output: 1 10000

Input: arr = [56789]
Output: 56789 56789'''

class Solution:
    def get_min_max(self, arr):
        n = len(arr)
        
        if n == 1:
            max_val = arr[0]
            min_val = arr[0]
        else:
            max_val = max(arr)
            min_val = min(arr)
        
        return [min_val, max_val]

sol = Solution()
arr = [3, 2, 1, 56, 10000, 167]
print(sol.get_min_max(arr))  # Expected Output: [1, 10000]

arr = [56789]
print(sol.get_min_max(arr))  # Expected Output: [56789, 56789]
