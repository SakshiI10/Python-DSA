'''Numbers have a measure of friendliness defined as the absolute difference between them. Given an circular array of integers arr[], calculate the friendliness of the array. Friendliness is the sum of the absolute differences between each element and its closest friend in the array.

Input: arr[] = [4, 1, 5]
Output: 8'''

class Solution:
    def calculateFriendliness(self, arr):
        n = len(arr)
        diff = 0
        
        for i in range(n):
            # Use modulo to handle the circular nature of the array
            abs_diff = abs(arr[(i + 1) % n] - arr[i])
            diff += abs_diff
        
        return diff

sol=Solution()
arr1 = [4, 1, 5]
print(f"Friendliness of arr1: {sol.calculateFriendliness(arr1)}")  # Output: 8
arr2 = [1, 1, 1]
print(f"Friendliness of arr2: {sol.calculateFriendliness(arr2)}")  # Output: 0
