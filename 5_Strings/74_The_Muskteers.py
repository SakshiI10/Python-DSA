'''
Given binary string str consisting of only 0's and 1's, Check if all the 0's are together or not.

Input:
str = "000"
Output:
YES'''

class Solution:
    def checkTogether(self, str):
        if '0' not in str:
            return 'NO'  

        first = str.find('0')
        last = str.rfind('0')

        for i in range(first, last + 1):
            if str[i] != '0':
                return 'NO'

        return 'YES'

sol=Solution()
str='11111'
print(sol.checkTogether(str))