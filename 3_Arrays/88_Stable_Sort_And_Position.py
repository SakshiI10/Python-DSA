class Solution:
    # Function to get the index of an element in a sorted array
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