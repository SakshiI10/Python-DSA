class Solution:
    # Brute Force
    def CountInversion(self, a, n):
        count=0
        for i in range(n):
            for j in range(i+1, n):
                if a[i]>a[j]:
                    count += 1
        return count
    
sol = Solution()
A = [5, 3, 2, 4, 1]
N = len(A)
output = sol.CountInversion(A, N)
print(output)
