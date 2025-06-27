'''
Given two strings s1 and s2 in lowercase, the task is to make them anagrams. The only allowed operation is to remove a character from any string. Find the minimum number of characters to be deleted to make both the strings anagram. Two strings are called anagrams of each other if one of them can be converted into another by rearranging its letters.

Input: s1 = "bcadeh", s2 = "hea"
Output: 3'''

class Solution:
    def remAnagram(self, s1, s2):
        l1 = list(s1)
        l2 = list(s2)
        count = 0

        for char in s1:
            if char in l2:
                l2.remove(char)
            else:
                count += 1

        count += len(l2)
        return count

sol=Solution()
s1 = "bcadeh"
s2 = "hea"
print(sol.remAnagram(s1, s2))