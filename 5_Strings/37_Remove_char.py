'''
Given two strings string1 and string2, remove those characters from first string(string1) which are present in second string(string2). Both the strings are different and contain only lowercase characters.
NOTE: Size of  first string is always greater than the size of  second string( |string1| > |string2|).

string1 = "computer"
string2 = "cat"
Output: "ompuer"'''

class Solution:
    def removeChars(self, string1, string2):
        res='' 
        for char in string1:
            if char not in string2:
                res += char 
        return res 

solution = Solution()
string1 = "computer"
string2 = "cat"
output = solution.removeChars(string1, string2)
print(output)  # Output: "ompuer"
