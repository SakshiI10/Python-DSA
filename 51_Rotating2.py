'''Given an array arr[]. The task is to rotate the array by d elements where d ≤ arr.size.

Input: arr[] = [-1, -2, -3, 4, 5, 6, 7], d = 2
Output: [-3, 4, 5, 6, 7, -1, -2]'''

class Solution:
    def leftRotate(self, arr, d):
        n = len(arr)
        d = d % n 
        arr[:] = arr[d:] + arr[:d]  

sol = Solution()
arr = [1, 2, 3, 4, 5]
sol.leftRotate(arr, 2)
print(arr)  

'''If arr[:] = ... is used, it modifies the original list in place, so no return is needed because When you return a value from a function, you're creating a new list instead of modifying the original one.
This is why this function works even without a return statement'''