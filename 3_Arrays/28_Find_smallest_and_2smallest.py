'''
Given an array, arr of integers, your task is to return the smallest and second smallest element in the array. If the smallest and second smallest do not exist, return -1.

Input: arr[] = [2, 4, 3, 5, 6]
Output: 2 3'''

class Solution:
    def minAnd2min(self, arr):
        n = len(arr)

        if n<2:
            return -1
        
        arr.sort()
        smallest=arr[0]
        sec_smallest=arr[1]

        if smallest==sec_smallest:
            return -1
        else:
            return smallest, sec_smallest

sol=Solution()
arr = [1, 1, 1]
print(sol.minAnd2min(arr))