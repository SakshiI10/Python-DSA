'''
Given an array arr, rotate the array by one position in clock-wise direction.
Input: arr = [1, 2, 3, 4, 5]
Output: [5, 1, 2, 3, 4]'''

class Solution:
    def left_rotate(self, arr, d):
        n = len(arr)
        d = d % n  
        return arr[d:] + arr[:d]

    def right_rotate(self, arr, d):
        n = len(arr)
        d = d % n  
        return arr[-d:] + arr[:-d]

sol=Solution()
arr = [9, 8, 7, 6, 4, 2, 1, 3]
d = 1
sol.left_rotate(arr, d)
sol.right_rotate(arr, d)

print(f"Original array: {arr}")
print(f"Array after left rotation by {d}: {sol.left_rotate(arr, d)}")
print(f"Array after right rotation by {d}: {sol.right_rotate(arr, d)}")
