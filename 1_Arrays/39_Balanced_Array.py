'''
Given an array arr of even size, the task is to find a minimum value that can be added to an element so that the array becomes balanced. An array is balanced if the sum of the left half of the array elements is equal to the sum of the right half.

Input: arr = [1, 5, 3, 2]
Output: 1'''

class Solution:
    def min_value_to_balance(self, arr):
        n = len(arr)
        k = n // 2
        
        sum1 = sum(arr[:k])
        sum2 = sum(arr[k:])
        
        return abs(sum1 - sum2)

sol = Solution()
arr = [1, 5, 3, 2]
result = sol.min_value_to_balance(arr)
print(result)  
