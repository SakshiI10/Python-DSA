'''
Given an array Arr of size N with all elements greater than or equal to zero. Return the maximum product of two numbers possible.

Input: 
N = 6
Arr[] = {1, 4, 3, 6, 7, 0}  
Output: 42'''

class Solution():
    def maxProduct(self, arr, n):
        arr.sort()
        product = arr[n-2] * arr[n-1]
        return product

sol = Solution()
N = 6
arr = [1, 4, 3, 6, 7, 0]
print(sol.maxProduct(arr, N))
