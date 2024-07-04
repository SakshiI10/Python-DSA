''' 
Given a stream of incoming numbers, find average or mean of the stream at every point.

Input:
n = 5
arr[] = {10, 20, 30, 40, 50}
Output: 10.00 15.00 20.00 25.00 30.00 '''

class Solution:
    def streamAvg(self, arr, n):
        current_sum = 0
        result = []
        
        for i in range(n):
            current_sum += arr[i]
            result.append(current_sum / (i + 1))
        
        return result

sol = Solution()
arr1 = [10, 20, 30, 40, 50]
n1 = len(arr1)
print(sol.streamAvg(arr1, n1))  # Output: [1.0, 1.5, 2.0, 2.5, 3.0]
