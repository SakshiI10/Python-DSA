''' 
Given a list of names, display the longest name. If there are multiple names of the longest size then return the first occurring name .

Input:
n = 5
names[] = { "Geek", "Geeks", "Geeksfor", "GeeksforGeek", "GeeksforGeeks" }
Output: GeeksforGeeks
Explanation: name "GeeksforGeeks" has maximum length among all names. '''

from typing import List

class Solution:
    def longest(self, n: int, names: List[str]) -> str:
        longest_name = ""
        max_length = 0
        
        for name in names:
            if len(name) > max_length:
                longest_name = name
                max_length = len(name)
        return longest_name

sol = Solution()
n = 5
names = ["Geek", "Geeks", "Geeksfor", "GeeksforGeek", "GeeksforGeeks"]
print(sol.longest(n, names))  # Output should be "GeeksforGeeks"