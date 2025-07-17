'''
Given a sorted array arr[] of n-1 integers, these integers are in the range of 1 to n. There are no duplicates in the array. One of the integers is missing in the array. Find the missing integer.

Input: arr[] = [1, 2, 3, 4, 6, 7, 8]
Output: 5'''

class Solution:
    def missingNumber(self, arr):
            arr.sort()
            n = len(arr)
            
            for i in range(n):
                if arr[i] != i + 1:
                    return i + 1
            return n + 1

sol=Solution()
arr = [1, 2, 3, 4, 6, 7, 8]
print(sol.missingNumber(arr))
