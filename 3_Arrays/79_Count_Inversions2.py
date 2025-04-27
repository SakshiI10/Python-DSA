class Solution:
    # Brute Force
    def CountInversion2(self, arr, brr, n1, n2):
        count=0
        for i in range(n1):
            for j in range(n2):
                if arr[i]>brr[j]:
                    count += 1
        return count
    
sol = Solution()
A = [2, 3, 5, 6]
B = [2, 2, 4, 4, 8]
N1 = len(A)
N2 = len(B)
output = sol.CountInversion2(A, B, N1, N2)
print(output)
