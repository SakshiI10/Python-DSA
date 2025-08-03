'''
Given an array arr[] of integers, determine whether a subsequence exists with an odd sum. If such a subsequence exists, return the maximum possible odd sum. If no subsequence with an odd sum can be formed, return -1.

Input: arr = [4, -3, 3, -5]
Output: 7

Input: arr = [2, 5, -4, 3, -1]
Output: 9'''

class Solution:
    def findMaxOddSum(self, arr):
        sum = 0
        isOdd = False
        min_odd = float('inf')

        for num in arr:
            if num > 0:
                sum += num
            if num % 2 != 0:
                isOdd = True
                if min_odd > abs(num):
                    min_odd = abs(num)

        if not isOdd:
            return -1
        if sum % 2 == 0:
            sum -= min_odd
        return sum

sol=Solution()
arr=[4, -3, 3, -5]
print(sol.findMaxOddSum(arr))  
