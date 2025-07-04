'''Given an array arr of n integers, sort the first half of the array in ascending order and second half in descending order.

Input:
n = 4
arr[] = {10, 20, 30, 40}
Output: 10 20 40 30 '''

class Solution:
    def customSort(self, arr, n):
        n=len(arr)
        k = n // 2
        
        first_half = sorted(arr[:k])
        second_half = sorted(arr[k:])
        second_half.reverse()
        
        print("Original Array:",arr)
        return "Altered Array",first_half + second_half

sol = Solution()
arr = [10, 20, 30, 40]
n = len(arr)
print(sol.customSort(arr, n))  