# Search smallest index: Use lower bound

class Solution:
    def insert_position(self, arr, k, n):
        low, high = 0, n-1
        ans = k

        while(low<=high):
            mid=(low+high)//2
            if arr[mid] >= k:
                ans=mid
                high=mid-1
            else:
                low=mid+1
        return ans
    
sol = Solution()
arr=[1, 2, 4, 7]
n=len(arr)
k1=2
k2=6
print(sol.insert_position(arr, k1, n))
print(sol.insert_position(arr, k2, n))
