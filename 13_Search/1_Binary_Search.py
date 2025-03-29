# Binary search is applicable when array is already sorted

class Solution:
    def binarysearch(self, arr, k):
        low, high = 0, len(arr) - 1
        
        while low <= high:
            mid = (low + high) // 2
            
            if arr[mid] == k:
                return mid
            elif arr[mid] < k:
                low = mid + 1
            else:
                high = mid - 1
        
        return -1
    
sol = Solution()
arr = [1, 2, 3, 4, 5]
k = 4
print(sol.binarysearch(arr, k))