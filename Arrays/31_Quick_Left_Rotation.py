'''
Given an array, arr[] of positive elements, and an integer k, the task is to left-rotate the array k indexes.

Input: arr[] = [1, 2, 3, 4, 5, 6, 7], k = 2 
Output: [3, 4, 5, 6, 7, 1, 2]'''

class Solution:
    def leftRotate(self, arr, k):
        n = len(arr)
        k = k % n  # Effective rotations
        return arr[k:] + arr[:k]  # Perform the rotation

sol = Solution()
print(sol.leftRotate([1, 2, 3, 4, 5, 6, 7], 2))   # Output: [3, 4, 5, 6, 7, 1, 2]
print(sol.leftRotate([1, 2, 3, 4, 5, 6], 12))    # Output: [1, 2, 3, 4, 5, 6]
print(sol.leftRotate([1, 2, 3, 4, 5, 6], 11))    # Output: [6, 1, 2, 3, 4, 5]
