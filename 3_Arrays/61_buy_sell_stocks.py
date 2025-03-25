class Solution:
    def max_subarray(self, arr):
        n=len(arr)
        profit=0
        num=arr[0]

        for i in range(1, n):
            cost=arr[i]-num
            profit=max(profit, cost)
            num=mi1n(num, arr[i])
        return profit

sol=Solution()
arr=[7, 1, 5, 3, 6, 4]
print(sol.max_subarray(arr))
