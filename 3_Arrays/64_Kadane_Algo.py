class Solution:
    def max_subarray(self, arr):
        n=len(arr)
        sum=0
        max_sum=float('-inf')

        for i in range(n):
            sum += arr[i]
            if sum>max_sum:
                max_sum=sum
            if sum<0:
                sum=0
        return max_sum

sol=Solution()
arr=[-2, -3, 4, -1, -2, 1, 5, -3]
print(sol.max_subarray(arr))
