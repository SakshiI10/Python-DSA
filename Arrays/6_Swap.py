''' 
Given an array arr of size n, swap the kth element from the beginning with kth element from the end.

Input:
n = 8
k = 3
arr[] = {1, 2, 3, 4, 5, 6, 7, 8}
Output: {1, 2, 6, 4, 5, 3, 7, 8}'''

from typing import List
class Solution:
    def swapKth(self, n : int, k : int, arr : List[int]) -> None:
        start_index=k-1
        end_index=n-k
        arr[start_index], arr[end_index]=arr[end_index], arr[start_index]
 
sol = Solution()
arr = [1, 2, 3, 4, 5, 6, 7, 8]
sol.swapKth(8, 3, arr)
print(arr)