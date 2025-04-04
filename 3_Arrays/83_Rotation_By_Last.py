class Solution:
    def rotate(self, arr):
        if not arr: 
            return
        last_element = arr.pop() 
        arr.insert(0, last_element)

sol = Solution()
arr1 = [1, 2, 3, 4, 5]
sol.rotate(arr1) 
print(arr1)  
