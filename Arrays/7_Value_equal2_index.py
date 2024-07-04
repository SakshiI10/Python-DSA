''' 
Given an array Arr of N positive integers. Your task is to find the elements whose value is equal to that of its index value ( Consider 1-based indexing ).

Input:
N = 5
Arr[] = {15, 2, 45, 12, 7}
Output: 2
Explanation: Only Arr[2] = 2 exists here.'''

class Solution:
    def valueEqualToIndex(self, arr, n):
        result = []
        for i in range(n):
            if arr[i] == i + 1:  # 1-based index comparison
                result.append(i + 1)
        return result

sol = Solution()
arr = [15, 2, 45, 4, 7]
n = len(arr)
print(sol.valueEqualToIndex(arr, n))  # Output: [2, 4]
