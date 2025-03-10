# arr=[1, 1, 0, 1, 1, 1, 0, 1, 1]
# Output is 3

class Solution():
    def cons(self, arr):
        max_count=0
        count=0
        n=len(arr)

        for i in range(n):
            if arr[i]==1:
                count += 1
                max_count=max(max_count, count)
            else:
                count=0
        return max_count
    

sol=Solution()
arr=[1, 1, 0, 1, 1, 1, 0, 1, 1]
print(sol.cons(arr))