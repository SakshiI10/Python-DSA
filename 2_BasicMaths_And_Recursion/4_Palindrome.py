''' 
Given a Integer array A[] of n elements. Your task is to complete the function PalinArray. Which will return 1 if all the elements of the Array are palindrome otherwise it will return 0.

Input:
5
111 222 333 444 555
Output: 1'''

class Solution:
    def isPalindrome(self, n):
        s = str(n)
        return s == s[::-1]

    def isPalinArray(self, arr, n):
        for num in arr:
            if not self.isPalindrome(num):
                return 'false'
        return 'true'

# Test
sol = Solution()
print(sol.isPalinArray([111, 222, 333, 444, 555], 5))  
print(sol.isPalinArray([121, 131, 20], 3))             

