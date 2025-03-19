class Solution:
    # Time Complexity: O(n2)
    # Space Complexity: O(n2)
    def rotate(self, arr, n, m):
        # _ is used in the for loop to iterate m times.
        ans = [[0] * n for _ in range(n)] 

        for i in range(n):
            for j in range(m):
                ans[j][n - 1 - i] = arr[i][j]
        return ans  

    # Time Complexity = 𝑂(𝑛2)
    def rotate2(self, arr, n, m):
        # Transpose the matrix
        for i in range(n):
            for j in range(i+1,m):
                arr[i][j], arr[j][i] = arr[j][i], arr[i][j]
        # Reverse each row
        for i in range(n):
            arr[i].reverse()

        return arr

arr = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16]
]
n, m = 4, 4
sol = Solution()

modified_matrix = sol.rotate(arr, n, m)
for row in modified_matrix:
    print(row)

print()

modified_matrix2 = sol.rotate2(arr, n, m)
for row in modified_matrix2:
    print(row)
