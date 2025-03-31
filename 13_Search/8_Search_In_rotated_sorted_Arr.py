# Can't use previous algo here for duplicate case. 
# Problem that may arise: arr[low=arr[mid]]=arr[high]

class Solution:
    def find(self, arr, target, n):
        low, high=0, n-1  
        while(low<=high):
            mid=(low+high)//2

            if arr[mid]==target:
                return mid
            
            if (arr[mid] == arr[mid] and arr[mid] == arr[high]):
                low += 1
                high -= 1
                continue

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
arr=[7, 8, 1, 2, 3, 3, 3, 4, 5, 6]
n=len(arr)
target=3
print(sol.find(arr, target, n))