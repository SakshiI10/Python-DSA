'''
Given a number N, count the numbers from 1 to N which comprise of digits only from set {1, 2, 3, 4, 5}.

Input: N = 20
Output: 10'''

class Solution:
    def countNumbers(self, N):
        valid_digits = {'1', '2', '3', '4', '5'}
        count = 0

        for num in range(N):  # Starts from 0 to N-1 and is not an index
            if num > 0 and set(str(num)).issubset(valid_digits): 
                count += 1

        return count

N = 20
sol = Solution()
print(sol.countNumbers(N))  # Output: 10
