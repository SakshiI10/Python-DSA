'''
Given an array of positive integers. The task is to print the minimum product of any two numbers of the given array.

Input : n = 4 arr[] = {2, 7, 3, 4}
Output : 6'''

class Solution:
    def printMinimumProduct(self, a, n):
        # Convert the list elements to integers if they are not already
        a = list(map(int, a))
        a.sort()
        result = a[0] * a[1]
        
        return result

sol = Solution()
arr = [2, 7, 3, 4]
n = len(arr)
print(sol.printMinimumProduct(arr, n))  # Expected Output: 6
