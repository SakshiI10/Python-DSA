# Floor: Largent no in an Array, such that x <= k
# Cail: Smalled no in an Array, such that x >= k: lower bound 

class Solution:
    def floor(self, arr, k, n):
        low, high = 0, n-1
        ans = -1

        while(low<=high):
            mid=(low+high)//2
            if arr[mid] <= k:
                ans=mid
                low=mid+1
            else:
                high=mid-1
        return ans
    
sol = Solution()
arr=[10, 20, 30, 40, 50]
n=len(arr)
k = 25
print(sol.floor(arr, k, n))