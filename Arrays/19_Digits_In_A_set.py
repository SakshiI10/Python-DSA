'''
Given a number N, count the numbers from 1 to N which comprise of digits only from set {1, 2, 3, 4, 5}.

Input: N = 20
Output: 10'''

class Solution:
    def countNumbers(self, N):
        valid_digits = {'1', '2', '3', '4', '5'}
        count = 0
        result = []

        for num in range(1, N + 1):
            if all(digit in valid_digits for digit in str(num)):
                count += 1
                result.append(num)

        return result, count

N = 20
sol = Solution()
print(sol.countNumbers(N))  # Output: 10
