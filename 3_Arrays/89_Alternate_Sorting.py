# Given an array arr of distinct integers. Rearrange the array in such a way that the first element is the largest and the second element is the smallest, the third element is the second largest and the fourth element is the second smallest, and so on.

# Input: arr[] = [7, 1, 2, 3, 4, 5, 6]
# Output: [7, 1, 6, 2, 5, 3, 4]

class Solution:
    def alternateSort(self,arr):
        n = len(arr)
        arr.sort()
        res = []
        i, j = 0, n - 1
        
        for k in range(n):
            if k % 2 == 0:
                res.append(arr[j])
                j -= 1
            else:
                res.append(arr[i])
                i += 1
                
        return res
    
sol=Solution()
arr=[7, 1, 2, 3, 4, 5, 6]
print(sol.alternateSort(arr))