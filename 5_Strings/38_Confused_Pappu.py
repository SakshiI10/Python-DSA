'''
Pappu is confused between 6 & 9. He works in the billing department of abc company and his work is to return the remaining amount to the customers. If the actual remaining amount is given we need to find the maximum possible extra amount given by the pappu to the customers.

Input: amount = 56
Output: 3
Explanation: maximum possible extra amount = 59 - 56 = 3.'''

class Solution:
    def findDiff(self, amount):
        num=''
        for char in str(amount):
            if char=='6':
                num += '9'
            else:
                num += char
                
        diff=abs(int(num)-amount)
        return diff

sol = Solution()
amount = 56
output = sol.findDiff(amount)
print(output)  # Output: 3
