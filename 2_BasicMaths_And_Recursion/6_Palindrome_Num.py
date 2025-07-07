'''
Given an array arr, the task is to find whether the arr is palindrome or not. 

Input: n=9987
Output: true'''

class Solution:
    def isPerfect(self, n):
        arr=list(str(n))
        n = len(arr)
        for i in range(n // 2):
            if arr[i] != arr[n - 1 - i]:
                return False
        return True
    
sol=Solution()
n=131
print(sol.isPerfect(n)) 