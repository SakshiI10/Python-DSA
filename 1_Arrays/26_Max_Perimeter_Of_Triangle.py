
'''
Given an Array of non-negative integers. Find out the maximum perimeter of the triangle from the array.

Input : arr[ ] = {6, 1, 6, 5, 8, 4}
Output : 20
'''

class Solution():
    def maxPerimeter (self, arr, n) : 
        arr.sort()
        
        for i in range(n - 1, 1, -1):
            if arr[i - 2] + arr[i - 1] > arr[i]:
                return arr[i - 2] + arr[i - 1] + arr[i]
        
        return -1

sol=Solution()
arr = [6, 1, 6, 5, 8, 4]
n=len(arr)
print(sol.maxPerimeter(arr, n))