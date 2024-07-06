'''
Given an array arr[] of N distinct integers, output the array in such a way that the first element is first maximum and the second element is the first minimum, and so on.

Input: N = 7, arr[] = {7, 1, 2, 3, 4, 5, 6}
Output: 7 1 6 2 5 3 4'''

class Solution:
    def alternateSort(self, arr, N):
        arr.sort()  
        result = []
        left, right = 0, N - 1
        
        for i in range(N):
            if i % 2 == 0:
                result.append(arr[right])  # Append from the sorted array 'arr'
                right -= 1
            else:
                result.append(arr[left])  # Append from the sorted array 'arr'
                left += 1
        
        return result
    
sol = Solution()
N = 7
arr = [7, 1, 2, 3, 4, 5, 6]
print(sol.alternateSort(arr, N))