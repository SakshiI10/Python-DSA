''' 
Given a sorted array Arr of size N and a value X, find the number of array elements less than or equal to X and elements more than or equal to X. 

Input:
N = 7, X = 0
Arr[] = {1, 2, 8, 10, 11, 12, 19}
Output: 0 7
Explanation: There are no elements less or
equal to 0 and 7 elements greater or equal
to 0.'''

class Solution:
    def getMoreAndLess(self, arr, n, x):
        less = 0
        more = 0
        for num in arr:
            if num <= x:
                less += 1
            if num >= x:
                more += 1
        return less, more

sol = Solution()
print(sol.getMoreAndLess([1, 2, 8, 10, 11, 12, 19], 7, 0))  # Output: (0, 7)
print(sol.getMoreAndLess([1, 2, 8, 10, 11, 12, 19], 7, 5))  # Output: (2, 5)
