'''
Given an array arr, you need to reverse a subarray of that array. The range of this subarray is given by indices l and r (1-based indexing).

Examples:

Input: arr[] = [1, 2, 3, 4, 5, 6, 7], l = 2, r = 4
Output: [1, 4, 3, 2, 5, 6, 7]'''

class Solution:
	def reverseSubArray(self,arr,l,r):
		l-=1
		r-=1
		while l < r:
			arr[l], arr[r] = arr[r], arr[l] 
			l += 1          
			r -= 1  
		return arr

sol= Solution()
arr = [1, 2, 3, 4, 5, 6, 7]
l = 2   
r = 4
print(sol.reverseSubArray(arr, l, r)) 