'''
Given two unsorted arrays a[] and b[] each consisting of distinct elements , the task is to return the of elements in the union of the two arrays in sorted order.

Input: a[] = [89, 24, 75, 11, 23], b[] = [89, 2, 4]
Output: [2, 4, 11, 23,  24, 75, 89]
'''

class Solution:
    def union(self, a, b):
        res=set()
        
        for num in a:
            res.add(num)
        for num in b:
            res.add(num)
            
        return sorted(res)

sol=Solution()
arr1=[1, 1, 2, 3, 4, 5]
arr2=[2, 3, 4, 4, 5, 6]
print(sol.union(arr1, arr2))
