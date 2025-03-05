'''
Given an array arr[] of integers, change the given array such that at any index i it contains the sum of all elements except itself. 
Simple way arr[i] should be arr[0] + arr[1] ... arr[i-1] + arr[i+1] ... arr[n-1].

Input: [3, 6, 4, 8, 9]
Output: [27, 24, 26, 22, 21]'''

class Solution:
    def sumArray(self, arr):
        n = len(arr)
        total_sum = sum(arr)
        result = []
        
        for i in range(n):
            result.append(total_sum - arr[i])
        
        return result

sol = Solution()
print(sol.sumArray([3, 6, 4, 8, 9])) 
