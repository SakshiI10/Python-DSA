# Given an array arr[] of n positive integers. The task is to find the maximum for every adjacent pairs in the array.

# Input:
# n = 6, arr[] = {1,2,2,3,4,5}
# Output: 2 2 3 4 5

class Solution:
    def maximumAdjacent(self, sizeOfArray, arr):
        res = []
        for i in range(sizeOfArray - 1): 
            res.append(max(arr[i], arr[i + 1]))
        print(*res)

sol = Solution()
sol.maximumAdjacent(6, [1, 2, 2, 3, 4, 5])  
 
