'''
Given an unsorted array arr, rearrange the array elements such that the number at the odd index is greater than the number at the previous even index.

Input: arr[] = [5, 4, 3, 2, 1]
Output: true'''

class Solution:
    def formatArray(self, arr):
        arr.sort()  
        n = len(arr)
        
        for i in range(1, n, 2):
            if arr[i] <= arr[i - 1]:
                arr[i], arr[i - 1] = arr[i - 1], arr[i]
                print(arr)
                return 'false'
        print(arr)
        return 'true'

sol = Solution()

arr1 = [5, 4, 3, 2, 1]
print(sol.formatArray(arr1))  
arr2 = [4, 3, 1, 1]
print(sol.formatArray(arr2))  
