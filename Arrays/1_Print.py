'''
Given an array arr of size n, print all its elements space-separated.

Input:
n = 5
arr[] = {1, 2, 3, 4, 5}
Output: 1 2 3 4 5'''

class Solution:
	def printArray(self, arr, n):
	   for i in range(n):
            print(arr[i], end=" ")

sol = Solution()		
n = 4
arr = [2, 3, 5, 5]
sol.printArray(arr, n)