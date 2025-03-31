# Search smallest index: Use lower bound

class Solution:
    def binarysearch(self, arr, target):
        n=len(arr)
        low, high = 0, n-1
        ans = target

        while(low<=high):
            mid=(low+high)//2
            if arr[mid] >= target:
                ans=mid
                high=mid-1
            else:
                low=mid+1
        return ans
    
sol = Solution()
arr=[1, 2, 4, 7]
k1=2
k2=6
print(sol.binarysearch(arr, k1))
print(sol.binarysearch(arr, k2))
