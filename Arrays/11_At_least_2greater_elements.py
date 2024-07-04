''' 
Given an array of N distinct elements, the task is to find all elements in array except two greatest elements in sorted order.

Input : 
a[] = {2, 8, 7, 1, 5}
Output :
1 2 5 
Explanation :
The output three elements have two or
more greater elements.   '''

class Solution:
    def findElements(self, a, n):
        arr_sorted = sorted(a)  
        result = arr_sorted[:-2]
        return result

sol = Solution()
arr = [2, 8, 7, 1, 5]
n = len(arr)
output = sol.findElements(arr, n)
print(output)  