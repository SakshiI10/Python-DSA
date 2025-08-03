# Given an array arr of distinct integers. Rearrange the array in such a way that the first element is the smallest and the second element is the largest, the third element is the second smallest and the fourth element is the second largest, and so on.

# Input: arr[] = [4, 5, 1, 2, 3]
# Output: [1, 5, 2, 4, 3]

class Solution:    
    def Rearrange(self, arr):
        n=len(arr)
        arr.sort()
        res=[]
        i, j=0, len(arr)-1
        
        for k in range(n):
            if k % 2 == 0:
                res.append(arr[i])
                i += 1
            else:
                res.append(arr[j])
                j -= 1
                
        return res
    
sol=Solution()
arr = [4, 5, 1, 2, 3]
print(sol.Rearrange(arr))  
