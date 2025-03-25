class Solution:
    #Brute Force
    def sorted(self, arr):
        arr.sort()
        return arr
    
    #pointer
    def sorted2(self, arr):
        n=len(arr)
        low, mid, high=0, 0, n-1

        for i in range(n):
            if arr[mid]==0:
                arr[low], arr[mid] = arr[mid], arr[low]
                low += 1
                mid += 1
            elif arr[mid]==1:
                mid += 1
            else:
                arr[mid], arr[high] = arr[high], arr[mid]
                high -= 1
        return arr

sol=Solution()
arr=[0, 1, 1, 0, 1, 2, 1, 2, 0, 0, 0]
print(sol.sorted(arr))
print(sol.sorted2(arr))
