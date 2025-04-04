class Solution:
    def game_with_number(self, arr, n):
        res = []
        
        for i in range(n - 1):  # Iterate up to the second-to-last element
            res.append(arr[i] ^ arr[i + 1])
        
        # Append the last element as it is to the result
        res.append(arr[-1])
        
        return res

sol=Solution()
arr = [10, 11, 1, 2, 3]
n = len(arr)
result = sol.game_with_number(arr, n)
print(result)
