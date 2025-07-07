'''
Given an odd number in the form of string, the task is to make largest even number possible from the given number provided one is allowed to do exactly only one swap operation, if no such number is possible then return the input string itself.

Input:
s = 4543
Output: 4534'''
# PRACTICE AGAIN

class Solution:
    def makeEven(self, s):
        n = len(s)
        s_list = list(s)
        last_digit = s_list[-1]
        swap_idx = -1

        for i in range(n - 1):
            if int(s_list[i]) % 2 == 0:
                swap_idx = i
                if s_list[i] < last_digit:
                    break

        if swap_idx == -1:
            return s 

        s_list[swap_idx], s_list[-1] = s_list[-1], s_list[swap_idx]
        return ''.join(s_list)
    
sol=Solution()
s='4543'
print(sol.makeEven(s))