'''
Given an array arr[] of distinct integers from 1 to arr.size(), count the minimum number of moveToFront operations needed to arrange the elements in ascending order (1, 2, 3, ..., arr.size()). A moveToFront operation picks any element arr[i] and places it at the first position.

Input: arr = [3, 2, 1, 4]
Output: 2

Input: arr = [5, 7, 4, 3, 2, 6, 1]
Output: 6 '''

class Solution:
    def minMoves(self, arr):
        n = len(arr)
        expected = n 
        
        for i in range(n - 1, -1, -1):
            if arr[i] == expected:
                expected -= 1
        
        return expected 
    
sol=Solution()
arr = [5, 7, 4, 3, 2, 6, 1]  
print(sol.minMoves(arr))  
