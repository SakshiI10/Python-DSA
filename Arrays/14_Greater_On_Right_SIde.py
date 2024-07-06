'''
ou are given an array Arr of size N. Replace every element with the next greatest element (greatest element on its right side) in the array. Also, since there is no element next to the last element, replace it with -1.

Input:
N = 6
Arr[] = {16, 17, 4, 3, 5, 2}
Output: 17 5 5 5 2 -1'''

class Solution:
	def nextGreatest(self,arr, n):
		max_right = -1
		
		for i in range(n-1, -1, -1):
		    current = arr[i]
		    arr[i] = max_right
		    if current > max_right:
		        max_right = current
		return arr

sol = Solution()
arr1 = [16, 17, 4, 3, 5, 2]
sol.nextGreatest(arr1, len(arr1))
print(arr1)  # Output: [17, 5, 5, 5, 2, -1]

arr2 = [2, 3, 1, 9]
sol.nextGreatest(arr2, len(arr2))
print(arr2)  # Output: [9, 9, 9, -1]
