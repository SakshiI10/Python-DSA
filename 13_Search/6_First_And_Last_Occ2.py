class Solution:
    def first_occurrence(self, arr, target, n):
        low, high = 0, n - 1
        first = -1

        while low <= high:
            mid = (low + high) // 2
            if arr[mid] == target:
                first = mid 
                high = mid - 1  
            elif arr[mid] < target:
                low = mid + 1
            else:
                high = mid - 1
        return first

    def last_occurrence(self, arr, target, n):
        low, high = 0, n - 1
        last = -1

        while low <= high:
            mid = (low + high) // 2
            if arr[mid] == target:
                last = mid  
                low = mid + 1 
            elif arr[mid] < target:
                low = mid + 1
            else:
                high = mid - 1
        return last

    def find(self, arr, target, n):
        first = self.first_occurrence(arr, target, n)
        last = self.last_occurrence(arr, target, n)
        return first, last

sol = Solution()
arr = [2, 4, 6, 8, 8, 8, 11, 11, 13]
n = len(arr)
target = 8
print(sol.find(arr, target, n))  # Expected Output: (3, 5)
