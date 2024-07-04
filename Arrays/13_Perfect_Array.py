'''
Given an array arr of size n and you have to tell whether the arr is perfect or not. An array is said to be perfect if its reverse array matches the original array. If the arr is perfect then return True else return False.

Input :
n = 5
arr = {1, 2, 3, 2, 1}
Output : PERFECT'''

from typing import List

class Solution:
    def isPerfect(self, n: int, arr: List[int]) -> bool:
        return arr == arr[::-1]

# Example usage:
n = 5
arr = [1, 2, 3, 2, 1]
solution = Solution()
if solution.isPerfect(n, arr):
    print("PERFECT")
else:
    print("NOT PERFECT")

    