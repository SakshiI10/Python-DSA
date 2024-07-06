''' 
Given an array of N distinct elements, the task is to find all elements in array except two greatest elements in sorted order.

Input : 
a[] = {2, 8, 7, 1, 5}
Output : 1 2 5'''

class Solution:
    def findElements(self, arr, n):
        arr.sort()
        result = arr[:-2]
        return result

sol = Solution()
arr = [2, 8, 7, 1, 5]
n = len(arr)
output = sol.findElements(arr, n)
print(output)  