'''
Remove character
Difficulty: BasicAccuracy: 59.6%Submissions: 47K+Points: 1
Given two strings string1 and string2, remove those characters from first string(string1) which are present in second string(string2). Both the strings are different and contain only lowercase characters.
NOTE: Size of  first string is always greater than the size of  second string( |string1| > |string2|).

string1 = "computer"
string2 = "cat"
Output: "ompuer"'''

class Solution:
    def removeChars(self, string1, string2):
        char_set = set(string2)
        filtered_chars = []
        for char in string1:
            if char not in char_set:
                filtered_chars.append(char)
        result = ''.join(filtered_chars)
        return result

solution = Solution()
string1 = "computer"
string2 = "cat"
output = solution.removeChars(string1, string2)
print(output)  # Output: "ompuer"
