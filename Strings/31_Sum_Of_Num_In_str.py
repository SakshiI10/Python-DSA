'''
Given a string str containing alphanumeric characters. The task is to calculate the sum of all the numbers present in the string.

Input:
str = 1abc23
Output: 24'''

class Solution:
    # Function to calculate the sum of all numbers present in a string.
    def findSum(self, s):
        total_sum = 0
        current_number = ''

        for char in s:
            if char.isdigit():
                current_number += char
            else:
                if current_number:
                    total_sum += int(current_number)
                    current_number = ''
        
        # Add the last number if there's any
        if current_number:
            total_sum += int(current_number)
        
        return total_sum

sol = Solution()
print(sol.findSum("1abc23"))  # Output: 24
print(sol.findSum("abc123xyz456"))  # Output: 579
print(sol.findSum("abc"))  # Output: 0
print(sol.findSum("1234"))  # Output: 1234
