'''
1. There must be a constant difference between the height of pillars (not zero) of a track. For eg., if the heights of first two pillars are 7 and 5, then height of 3rd pillar must be 3. As 7-5=2 & 5-3=2.

2. The height of middle pillar must be always 1.

3. Number of pillars on the left side must be equal to the number of pillars on the right side of middle pillar. And their heights must be also equal. for example: Track with pillar heights [3 2 1 2 3] is a valid track. 

N = 3
A[] = {2, 1, 2}
Output: Yes'''

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
