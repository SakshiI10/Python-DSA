'''
Given an array arr[] of non-negative integers, determine whether the array is perfect. An array is considered perfect if it first strictly increases, then remains constant, and finally strictly decreases. Any of these three parts can be empty.

Input: arr[] = [1, 8, 8, 8, 3, 2]
Output: true'''

class Solution:
    def isPerfect(self, arr):
        n=len(arr)

        i=0
        while i+1<n and arr[i]<arr[i+1]:
            i += 1
        while i+1<n and arr[i]==arr[i+1]:
            i += 1
        while i+1<n and arr[i]>arr[i+1]:
            i += 1
            
        return i==n-1
            
sol=Solution()
arr=[1, 8, 8, 8, 3, 2]
print(sol.isPerfect(arr))  
