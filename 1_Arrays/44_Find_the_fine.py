'''
Given an array of car numbers car[], an array of penalties fine[], and an integer value date. The task is to find the total fine which will be collected on the given date. The fine is collected from odd-numbered cars on even dates and vice versa.

Input: date = 12, car[] = [2375, 7682, 2325, 2352], fine[] = [250, 500, 350, 200]
Output: 600'''

class Solution:
    def totalFine(self, date, car, fine):
        n = len(car)
        total_fine = 0
        
        for i in range(n):
            if date % 2 == 0:
                if car[i] % 2 != 0: 
                    total_fine += fine[i]
            else:
                if car[i] % 2 == 0:  
                    total_fine += fine[i]
                    
        return total_fine

date = 12
car = [2375, 7682, 2325, 2352]
fine = [250, 500, 350, 200]

solution = Solution()
print(solution.totalFine(date, car, fine))  # Output: 600
