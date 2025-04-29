'''
Given an array nums of positive integers of size N. Find all distinct digits present in nums.

Input: nums = [131, 11, 48]
Output: 1 3 4 8'''

class Solution:
	def common_digits(self, nums):
		res=set()
		
		for num in nums:
			for ch in str(num):
				res.add(int(ch))
		    
		return sorted(res)
	
sol=Solution()
arr=[131, 11, 48]
print(sol.common_digits(arr))

# set.add(x) ➔ adds a single element x to the set.
# set.update(iterable) ➔ adds all elements from an iterable (like list, string, tuple) into the set.