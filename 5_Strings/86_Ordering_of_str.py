'''
You will be given N number of strings. You have to find the lexicographically smallest string and the lexicographically largest string among these strings.

Input:
N = 3
strings = a , ab , abc
Output: a abc'''

class Solution:
    def orderString(self, s, n):
        smallest = s[0]
        largest = s[0]

        for string in s[1:]:
            if string < smallest:
                smallest = string
            if string > largest:
                largest = string

        return (smallest, largest)
    
sol=Solution()
N = 3
s = "a ab abc".split()
print(sol.orderString(s, N))