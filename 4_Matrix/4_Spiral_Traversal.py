class Solution:
    def spiralOrder(self, arr, n, m):
        left, right, top, bottom = 0, m - 1, 0, n - 1
        result = []

        while top <= bottom and left <= right:
            # Traverse from left to right
            for i in range(left, right + 1):
                result.append(arr[top][i])
            top += 1

            # Traverse from top to bottom
            for i in range(top, bottom + 1):
                result.append(arr[i][right])
            right -= 1

            # Traverse from right to left
            if top <= bottom:
                for i in range(right, left - 1, -1):
                    result.append(arr[bottom][i])
                bottom -= 1

            # Traverse from bottom to top
            if left <= right:
                for i in range(bottom, top - 1, -1):
                    result.append(arr[i][left])
                left += 1

        return result  

arr = [
    [1, 2, 3, 4, 5, 6],
    [20, 21, 22, 23, 24, 7],
    [19, 32, 33, 34, 25, 8],
    [18, 31, 30, 29, 26, 9],
    [17, 16, 15, 14, 13, 12]
]

n, m = 5, 6
sol = Solution()
spiral_result = sol.spiralOrder(arr, n, m)
print("Spiral Order:", spiral_result)
