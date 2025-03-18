class Solution:
    def matrix(self, arr, n, m):
        row = [0] * n  
        col = [0] * m  

        for i in range(n):
            for j in range(m):
                if arr[i][j] == 0:
                    row[i] = 1
                    col[j] = 1

        for i in range(n):
            for j in range(m):
                if row[i] == 1 or col[j] == 1:
                    arr[i][j] = 0

        zero_count = sum(num == 0 for row in arr for num in row)
        return arr, zero_count

arr = [
    [1, 1, 1, 1],
    [1, 0, 1, 1],
    [1, 1, 0, 1],
    [1, 1, 1, 1]
]
n, m = 4, 4
sol = Solution()
modified_matrix, zero_count = sol.matrix(arr, n, m)

for row in modified_matrix:
    print(row)
print("Count of zeros:", zero_count)
