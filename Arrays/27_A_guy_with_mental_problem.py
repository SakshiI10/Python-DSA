'''
A guy has to reach his home and does not want to be late. He takes train to reach home. He has a mental illness, so he always switches train at every station.
Input: N = 3
A[] = {2, 1, 2}
B[] = {3, 2, 1}
Output: 5'''

class Solution:
    def minTime(self, a, b, n):
        time_with_A = 0
        time_with_B = 0

        for i in range(n):
            if i % 2 == 0:
                time_with_A += a[i]
            else:
                time_with_A += b[i]

        for i in range(n):
            if i % 2 == 0:
                time_with_B += b[i]
            else:
                time_with_B += a[i]

        return min(time_with_A, time_with_B)

sol = Solution()
a = [2, 1, 2]
b = [3, 2, 1]
n = 3
print(sol.minTime(a, b, n))  # Output: 5
