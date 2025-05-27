'''
Given two arrays arr1[] and arr2[] of the same size, find the minimum sum of two elements such that one element is from arr1[] and the other is from arr2[], and they are not at the same index in their respective arrays.

Input: arr1[] = [5, 4, 13, 1], arr2[] = [3, 2, 6, 1]
Output: 3
'''

class Solution:
    def minSum(self, arr1, arr2):
        n = len(arr1)
        min1 = min(arr1)
        min2 = min(arr2)
        min1_index = arr1.index(min1)
        min2_index = arr2.index(min2)

        if min1_index != min2_index:
            return min1 + min2
            
        second_min1 = float('inf')
        second_min2 = float('inf')

        for i in range(n):
            if i != min2_index:
                second_min1 = min(second_min1, arr1[i])
            if i != min1_index:
                second_min2 = min(second_min2, arr2[i])

        return min(min1 + second_min2, second_min1 + min2)
    
sol = Solution()
arr1 = [5, 4, 13, 1]    
arr2 = [3, 2, 6, 1]
print(sol.minSum(arr1, arr2))  
