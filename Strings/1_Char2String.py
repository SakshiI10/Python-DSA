'''
Convert character to String'''

class Solution:
    def chartostr(self, arr, n):
        result = ""
        for i in range(n):
            result += arr[i]
        return result

sol = Solution()
n = 6
arr = ['q', 'w', 'e', 'r', 't', 'y']
print(sol.chartostr(arr, n))
