'''
Given two arrays of A and B respectively of sizes N1 and N2, the task is to calculate the product of the maximum element of the first array and minimum element of the second array.

Input : A[] = {5, 7, 9, 3, 6, 2}, 
        B[] = {1, 2, 6, -1, 0, 9}
Output : -9'''

class Solution:
    def find_multiplication(self, arr, brr, n, m):
        max_val = max(arr)
        min_val = min(brr)
        result = max_val * min_val
        return result

sol = Solution()
arr = [5, 7, 9, 3, 6, 2]
n = len(arr)
brr = [1, 2, 6, -1, 0, 9]
m = len(brr)
print(sol.find_multiplication(arr, brr, n, m))

