class Solution:
    def max_subarray(self, arr):
        #Brute Force
        n=len(arr)
        max_sum=0

        for i in range(n):
            sum=0
            for j in range(i, n):
                sum += arr[j]
                max_sum=max(max_sum, sum)
        return max_sum

sol=Solution()
arr=[-2, -3, 4, -1, -2, 1, 5, -3]
print(sol.max_subarray(arr))
