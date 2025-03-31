class Solution:
    def lower_bound(self, arr, target, n):
        low, high = 0, n-1
        ans = n

        while(low<=high):
            mid=(low+high)//2
            if arr[mid] >= target:
                ans=mid
                high=mid-1
            else:
                low=mid+1
        return ans

    def upper_bound(self, arr, target, n):
        low, high = 0, n-1
        ans = n

        while(low<=high):
            mid=(low+high)//2
            if arr[mid] > target:
                ans=mid
                high=mid-1
            else:
                low=mid+1
        return ans

sol=Solution()
arr=[1, 2, 3, 3, 5, 8, 8, 10, 11]
n=len(arr)
target=9
print(sol.lower_bound(arr, target, n))
target=6
print(sol.upper_bound(arr, target, n))