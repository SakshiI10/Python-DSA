'''
Given an array arr of size n and you have to tell whether the arr is perfect or not. An array is said to be perfect if its reverse array matches the original array. If the arr is perfect then return True else return False.

Input :
n = 5
arr = {1, 2, 3, 2, 1}
Output : PERFECT'''

from typing import List

class Solution:
    def isPerfect(self, n, arr):
        return arr == arr[::-1]

n = 5
arr = [1, 2, 3, 2, 1]
sol = Solution()
if sol.isPerfect(n, arr):
    print("PERFECT")
else:
    print("NOT PERFECT")
