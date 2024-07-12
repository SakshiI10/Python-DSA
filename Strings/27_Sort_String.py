'''
Given a string str containing only lower case alphabets, the task is to sort it in lexicographically-descending order.

Input: str = "geeks"
Output: "skgee" '''

class Solution:
    def ReverseSort(self, str): 
        sorted_str = ''.join(sorted(str))
        return sorted_str[::-1]

sol=Solution()
str="geeks"
print(sol.ReverseSort(str))