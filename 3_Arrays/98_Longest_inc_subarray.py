'''
Given an array arr[] of integers. The problem is finding the longest contiguous subarray's length such that every element is strictly greater than its previous element in the same subarray.

Input: arr[] = [5, 6, 3, 5, 7, 8, 9, 1, 2]
Output: 5'''

class Solution:
    def lenOfLongIncSubArr(self, arr):
        n=len(arr)
        length=1
        max_length=1
        
        for i in range(1, n):
            if arr[i]>arr[i-1]:
                length += 1
                max_length=max(max_length, length)
            else:
                length=1
                
        return max_length
    
sol=Solution()
arr=[5, 6, 3, 5, 7, 8, 9, 1, 2]
print(sol.lenOfLongIncSubArr(arr))
