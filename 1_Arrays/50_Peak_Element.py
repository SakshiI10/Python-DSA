'''Given an array arr[] where no two adjacent elements are same, find the index of a peak element. An element is considered to be a peak if it is greater than its adjacent elements (if they exist). If there are multiple peak elements, return index of any one of them. The output will be "true" if the index returned by your function is correct; otherwise, it will be "false".

Examples:
Input: arr = [1, 2, 4, 5, 7, 8, 3]
Output: true
Input: arr = [10, 20, 15, 2, 23, 90, 80]
Output: true'''

class Solution:   
    def peakElement(self, arr):
        n = len(arr)
        
        if n == 0:  # Edge case: Empty array
            return False  # No peak exists
        
        if n == 1:  # Single-element array
            return True
        
        # Check first element
        if arr[0] > arr[1]:
            return True
        
        # Check last element
        if arr[n-1] > arr[n-2]:
            return True
        
        # Check middle elements
        for i in range(1, n-1):
            if arr[i] > arr[i-1] and arr[i] > arr[i+1]:
                return True
        
        return False  # No peak found (shouldn't happen per constraints)

# Example usage:
arr = [1, 2, 4, 5, 7, 8, 3]
sol = Solution()
print(sol.peakElement(arr))  # Expected output: True
