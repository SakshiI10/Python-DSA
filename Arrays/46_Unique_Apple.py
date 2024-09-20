'''Given a queue of persons represented by an array of integers, where each person is identified by a specific integer, find the minimum kilograms of apples that need to be distributed, ensuring that each person receives 1 kilogram of apples only once.

Input: arr[] = [1, 1, 1, 1, 1]
Output: 1'''

class Solution:
    def minimumApple(self, arr):
        unique_persons = set(arr)
        # The minimum apples needed is the count of unique persons
        return len(unique_persons)

solution = Solution()
arr1 = [1, 1, 1, 1, 1]
print("Minimum apples required for arr1:", solution.minimumApple(arr1))  # Output: 1

arr2 = [1, 2, 3, 1, 2]
print("Minimum apples required for arr2:", solution.minimumApple(arr2))  # Output: 3
