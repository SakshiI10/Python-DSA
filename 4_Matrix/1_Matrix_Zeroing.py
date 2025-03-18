class Solution:
    #Brute Force: O(n3)
    def mark_row(self, arr, i, m):
        for j in range(m):
            if arr[i][j] != 0:
                arr[i][j] = -1

    def mark_col(self, arr, j, n):
        for i in range(n):
            if arr[i][j] != 0:
                arr[i][j] = -1

    def matrix(self, arr, n, m):
        for i in range(n):
            for j in range(m):
                if arr[i][j] == 0:
                    self.mark_row(arr, i, m)
                    self.mark_col(arr, j, n)

        for i in range(n):
            for j in range(m):
                if arr[i][j] == -1:
                    arr[i][j] = 0

        # Count number of zeros
        count = 0
        for row in arr:
            for num in row:
                if num == 0:
                    count += 1
        return count
    
arr = [
    [1, 1, 1, 1],
    [1, 0, 1, 1],
    [1, 1, 0, 1],
    [1, 1, 1, 1]
]
n, m = 4, 4
sol = Solution()
zero_count = sol.matrix(arr, n, m)

# Print the modified matrix and zero count
for row in arr:
    print(row)
print("Count of zeros:", zero_count)
