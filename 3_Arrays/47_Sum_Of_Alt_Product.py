'''
Given an array arr of even size consisting of positive integers. After sorting the array, find the sum of the product of i-th element from starting and i-th element from last.

Input: arr[] = [9, 2, 8, 4, 5, 7, 6, 0]
Output: 74'''
# [0, 2, 4, 5, 6, 7, 8, 9]

class Solution:
    def altProduct(self, arr):
        arr.sort()
        n = len(arr)
        print(arr)
        sum_alt = 0

        for i in range(n//2):
            product = arr[i]*arr[n-i-1]
            sum_alt += product
        
        return sum_alt

sol = Solution()
arr = [9, 2, 8, 4, 5, 7, 6, 0]
print(sol.altProduct(arr))  # Output: 74
