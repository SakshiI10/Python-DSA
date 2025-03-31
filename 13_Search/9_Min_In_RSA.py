class Solution:
    def find(self, arr, n):
        low, high=0, n-1  
        ans=float('inf')

        while(low<=high):
            mid=(low+high)//2

            if arr[low]<=arr[mid]:
                ans=min(ans, arr[low])
                low=mid+1
            else:
                high=mid-1
                ans=min(ans, arr[mid])
        return ans


sol=Solution()
arr1=[4, 5, 6, 7, 0, 1, 2]
n1=len(arr1)
arr2=[7, 8, 1, 2, 3, 4, 5, 6]
n2=len(arr2)
arr3=[4, 5, 1, 2, 3]
n3=len(arr3)

print(sol.find(arr1, n1))
print(sol.find(arr2, n2))
print(sol.find(arr3, n3))