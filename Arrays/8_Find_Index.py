'''
Given an unsorted array arr[] of n integers and a key which is present in this array. You need to write a program to find the start index (index where the element is first found from left in the array) and end index (index where the element is first found from right in the array). (0 based indexing is used). If the key does not exist in the array then return -1 for both start and end index in this case.

Input:
n = 6
arr[] = { 1, 2, 3, 4, 5, 5 }
key = 5
Output: {4, 5}'''

class Solution:
    def findIndex(self, arr, n, key):
        start_index = -1
        end_index = -1
        
        # Find the start index
        for i in range(n):
            if arr[i] == key:
                start_index = i
                break
        
        # Find the end index
        for i in range(n - 1, -1, -1):
            if arr[i] == key:
                end_index = i
                break
        
        return (start_index, end_index)

sol = Solution()
n = 6
arr = [1, 2, 3, 4, 5, 5]
key = 5
print(sol.findIndex(arr, n, key))  # Output: (4, 5)
       