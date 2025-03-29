class Solution:
    # Brute Force
    def MaxPro_Subarray(self, a, n):
        max_prod = float('-inf') 
        for i in range(n):
            prod = 1
            for j in range(i, n): 
                prod *= a[j]  
                max_prod = max(max_prod, prod) 

        return max_prod

sol = Solution()
A = [2, 3, -2, 4]
N = len(A)
output = sol.MaxPro_Subarray(A, N)
print(output)  