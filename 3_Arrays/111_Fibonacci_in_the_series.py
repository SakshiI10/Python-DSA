'''
Given an array arr of integers, the task is to count the number of elements of the array which are Fibonacci numbers.

Input: arr[] = [4, 2, 8, 5, 20, 1, 40, 13, 23]
Output: 5'''

class Solution:
    def countFibonacciNumbers(self, arr):        
        max_elem = max(arr)
        fib_set = set()
        a, b = 0, 1

        while a <= max_elem:
            fib_set.add(a)
            a, b = b, a + b
        # print(fib_set)

        print()
        count = 0
        for num in arr:
            if num in fib_set:
                count += 1
        
        return count

sol = Solution()
arr = [4, 2, 8, 5, 20, 1, 40, 13, 23]
print(sol.countFibonacciNumbers(arr))
