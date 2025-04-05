# Input: k = 10, arr1 = [3, 4, 5], arr2 = [4, 4, 5]
# Output: 12

class Solution:
    def maxPoint(self, k,arr1,arr2):
        n=len(arr1)
        max_points=0
        
        for i in range(n):
            max_reads = k//arr1[i]
            points = max_reads * arr2[i]
            max_points = max(max_points, points)
            
        return max_points
    
sol = Solution()
K = 10  
A = [3, 4, 5]  
B = [4, 4, 5]  

result = sol.maxPoint(K, A, B)
print("Maximum Points:", result)
