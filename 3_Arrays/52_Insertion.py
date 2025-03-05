'''You are given an array arr(0-based index). The size of the array is given by sizeOfArray. You need to insert an element at given index.
Input:
sizeOfArray = 6
arr[] = {1, 2, 3, 4, 5}
index = 5, element = 90
Output: 1 2 3 4 5 90'''

class Solution:
    def insertAtIndex(self, arr, sizeOfArray, index, element):
        for i in range(sizeOfArray - 1, index - 1, -1):
            arr[i] = arr[i - 1]
        
        arr[index] = element

sol = Solution()
arr = [1, 2, 3, 4, 5, 0]  
sizeOfArray = 6
index = 2
element = 90
sol.insertAtIndex(arr, sizeOfArray, index, element)
print(arr)
