'''
Given an array of N positive integers where all numbers occur even number of times except one number which occurs odd number of times. Find the exceptional number.

Input: N = 7
Arr[] = {1, 2, 3, 2, 3, 1, 3}
Output: 3 '''

class Solution:
    def find_odd_occurrence(self, arr):
        frequency = {}

        for num in arr:
            if num in frequency:
                frequency[num] += 1
            else:
                frequency[num] = 1

        for num, count in frequency.items():
            if count % 2 != 0:
                return num

sol=Solution()
arr1 = [1, 2, 3, 2, 3, 1, 3]
print(sol.find_odd_occurrence(arr1))  
