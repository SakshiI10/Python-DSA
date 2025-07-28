'''
Given an array arr[] and an integer k. You can perform an operation in which you can increment any of the number in the array by k. Find the minimum number of operations needed to make all the elements of array equal.

Input: arr[] = [4, 4, 4, 2], k = 2
Output: 1'''

class Solution:
    def minOps(self,arr, k):
        max_val = max(arr)
        operations = 0

        for a in arr:
            diff = max_val - a
            if diff % k != 0:
                return -1
            operations += diff // k

        return operations
    
sol=Solution()
arr=[4, 4, 4, 2]
k = 2
print(sol.minOps(arr, k))
