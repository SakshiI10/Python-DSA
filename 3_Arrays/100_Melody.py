'''
Chunky gets happy by eating Melody. Given an array arr[], each element represents the happiness Chunky gets by eating the melody.
Chunky knows why Melody is so chocolaty but will only tell you once you tell him the maximum happiness he can get by eating two adjacent melodies.

Input : arr[] = [1, 2, 3, 4, 5]
Output : 9'''

class Solution:
    def max_happiness(self, arr):
        n=len(arr)
        if n < 2:
            return 0  
        max_sum = arr[0] + arr[1]
        
        for i in range(1, n-1):
            current_sum = arr[i] + arr[i + 1]
            if current_sum > max_sum:
                max_sum = current_sum
        return max_sum
    
sol=Solution()
arr=[1, 2, 3, 4, 5]
print(sol.max_happiness(arr))
