class Solution():
    def is_valid_track(self, arr, n):
        if n % 2 == 0:
            return "No"
        
        mid_index = n // 2
        if arr[mid_index] != 1:
            return "No"
        
        difference = arr[0] - arr[1]
        if difference == 0:
            return "No"
        
        for i in range(mid_index):
            if arr[i] - arr[i + 1] != difference or arr[i] != arr[n - 1 - i]:
                return "No"
        
        return "Yes"

sol = Solution()
N = 3
A = [2, 1, 2]
print(sol.is_valid_track(A, N))  # Output: Yes
