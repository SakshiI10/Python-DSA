'''
Given an array arr integers that may contain duplicate elements, the index of an element of this array is given to us k (0-based indexing), the task is to find the final position of this element in the array after the stable sort is applied to the array. 

Input: arr[]= [3, 4, 3, 5, 2, 3, 4, 3, 1, 5], k = 5
Output: 4'''

class Solution:
    def getIndexInSortedArray(self, arr, k):
        with_index = [] 
        n = len(arr)
        
        for i in range(n):
            with_index.append((arr[i], i)) 

        with_index.sort(key=lambda x: x[0])
        m=len(with_index)
       
        for i in range(m):
            if with_index[i][1] == k: 
                return i
            
sol = Solution()
arr = [3, 4, 3, 5, 2, 3, 4, 3, 1, 5]
k = 5
result = sol.getIndexInSortedArray(arr, k)
print("New index of", k, "is:", result)
