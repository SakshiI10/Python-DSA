'''
Given an array, arr of n integers, and an integer element x, find whether element x is present in the array. Return the index of the first occurrence of x in the array, or -1 if it doesn't exist.

Input: arr[] = [1, 2, 3, 4], x = 3
Output: 2

Input: arr[] = [10, 8, 30, 4, 5], x = 5
Output: 4

Input: arr[] = [10, 8, 30], x = 6
Output: -1'''

class Solution:
    def search(self, arr, x):
        n=len(arr)
        for i in range(len(arr)):
            if arr[i] == x:
                return i
        return -1

sol = Solution()
print(sol.search([1, 2, 3, 4], 3))  # Output: 2
print(sol.search([10, 8, 30, 4, 5], 5))  # Output: 4
print(sol.search([10, 8, 30], 6))  # Output: -1
