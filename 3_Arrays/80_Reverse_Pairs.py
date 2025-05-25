class Solution:
    # Brute Force
    def CountPairs(self, a, n):
        count=0
        for i in range(n):
            for j in range(i+1, n):
                if a[i]>(2*a[j]):
                    count += 1
        return count
    
sol = Solution()
A = [40, 25, 19, 12, 9, 6, 2]
N = len(A)
output = sol.CountPairs(A, N)
print(output)
