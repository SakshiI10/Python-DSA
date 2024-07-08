'''
Given a number N, count the numbers from 1 to N which comprise of digits only from set {1, 2, 3, 4, 5}.

Input:
N = 20
Output: 10'''
# Need improvements

class Solution:
    def countNumbers(self, N):
        valid_digits = {'1', '2', '3', '4', '5'}
        count = 0
        
        for num in range(1, N + 1):
            if all(digit in valid_digits for digit in str(num)):
                count += 1
        
        return count

N = 20
solution = Solution()
print(solution.countNumbers(N))  # Output: 10
