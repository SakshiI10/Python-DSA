'''
Given an array arr, the task is to find whether the arr is palindrome or not. If the arr is palindrome then return true else return false.

Input: arr = [1, 2, 3, 2, 1]
Output: true'''

class Solution:
    def isPerfect(self, arr):
        n = len(arr)
        for i in range(n // 2):
            if arr[i] != arr[n - 1 - i]:
                return False
        return True
    
sol=Solution()
arr=[1, 2, 3, 2, 1]
print(sol.isPerfect(arr)) 