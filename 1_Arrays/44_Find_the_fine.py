'''
Given an array of car numbers car[], an array of penalties fine[], and an integer value date. The task is to find the total fine which will be collected on the given date. The fine is collected from odd-numbered cars on even dates and vice versa.

Input: date = 12, car[] = [2375, 7682, 2325, 2352], fine[] = [250, 500, 350, 200]
Output: 600'''

class Solution:
    def totalFine(self, date, car, fine):
        

date = 12
car = [2375, 7682, 2325, 2352]
fine = [250, 500, 350, 200]

solution = Solution()
print(solution.totalFine(date, car, fine))  # Output: 600
