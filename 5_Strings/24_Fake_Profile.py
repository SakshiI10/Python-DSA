'''
There is a hacker named "Vijay" who has developed a method to check whether an id at some social networking site is fake or real using its username.

His method includes: if the number of distinct consonent characters in one's user name is odd, then the user is a male, otherwise a female. You are given the string that denotes the user name, please help Vijay to determine the gender of this user by his method. Ignore the vowels.
Note: The input only contains lowercase English alphabets.

Input: a = "jpmztf"
Output: SHE!'''

class Solution:
    def solve(self, a):
        vowels = set('aeiou')
        cons = set()

        for char in a:
            if char not in vowels:
                cons.add(char)

        if len(cons) % 2 == 0:
            return 'SHE!'
        else:
            return 'HE!'

solution = Solution()
a = "jpmztf"
output = solution.solve(a)
print(output)  # Expected output: SHE!
