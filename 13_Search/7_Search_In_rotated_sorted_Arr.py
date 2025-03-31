# When search and sorted in problem statement use Binary Search.

class Solution:
    def find(self, arr, target, n):
        low, high=0, n-1  
        while(low<=high):
            mid=(low+high)//2

            if arr[mid]==target:
                return mid
              
            if (arr[low] <= arr[mid]):
                if (arr[low] <= target and target<=arr[mid]):
                    high=mid-1
                else:
                    low=mid+1
            else:
                if (arr[low] <= target and target<=arr[mid]):
                    low=mid+1
                else:
                    high=mid-1
        return -1       

sol=Solution()
arr=[7, 8, 9, 1, 2, 3, 4, 5, 6]
n=len(arr)
target=1
print(sol.find(arr, target, n))