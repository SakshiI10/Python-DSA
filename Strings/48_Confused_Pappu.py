'''
Pappu is confused between 6 & 9. He works in the billing department of abc company and his work is to return the remaining amount to the customers. If the actual remaining amount is given we need to find the maximum possible extra amount given by the pappu to the customers.

Input: amount = 56
Output: 3
Explanation: maximum possible extra amount = 59 - 56 = 3.'''

class Solution:
    def findDiff(self, amount):
        amount_str = list(str(amount))
        
        for i in range(len(amount_str)):
            if amount_str[i] == '6':
                amount_str[i] = '9'
        
        modified_amount = int(''.join(amount_str))
        diff = modified_amount - amount
        return diff

sol = Solution()
amount = 56
output = sol.findDiff(amount)
print(output)  # Output: 3
