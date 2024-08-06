'''
Given an array arr of integers and an index key(0-based index). Your task is to return the element present at the index key in the array.

Input: key = 2 , arr = [10, 20, 30, 40, 50]
Output: 30'''

from typing import List


class Solution:
    def findElementAtIndex(self, key : int, arr : List[int]) -> int:
        return arr[key]