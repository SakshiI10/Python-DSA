'''
Given an odd number in the form of string, the task is to make largest even number possible from the given number provided one is allowed to do exactly only one swap operation, if no such number is possible then return the input string itself.

Input:
s = 4543
Output: 4534 '''

class Solution:
    def makeEven(self, s):
        n = len(s)
        last_digit = int(s[-1])

        # If the last digit is even, return the original string
        if last_digit % 2 == 0:
            return s

        # Look for an even digit to swap with the last digit
        for i in range(n - 1):
            if int(s[i]) % 2 == 0:
                # Swap the first found even digit with the last digit
                s = list(s)
                s[i], s[-1] = s[-1], s[i]
                return ''.join(s)

        # If no even digit is found to make the swap, return the original string
        return s

solution = Solution()
print(solution.makeEven("4543"))  
print(solution.makeEven("123"))   
print(solution.makeEven("345"))   
