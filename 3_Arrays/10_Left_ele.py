''' 
Given a array of length N, at each step it is reduced by 1 element. In the first step the maximum element would be removed, while in the second step minimum element of the remaining array would be removed, in the third step again the maximum and so on. Continue this till the array contains only 1 element. And find the final element remaining in the array.

Input:
N = 7
A[] = {7, 8, 3, 4, 2, 9, 5}
Ouput: 5'''

class Solution:
    def leftElement(self, arr, n):
        arr.sort()

        for i in range(n):
            print(arr[i], end=" ")

        left_element = arr[(n - 1) // 2]
        result = [left_element]

        return result

solution = Solution()
N1 = 7
A1 = [7, 8, 3, 4, 2, 9, 5]
print(solution.leftElement(A1, N1))  # Output: 5

N2 = 8
A2 = [8, 1, 2, 9, 4, 3, 7, 5]
print(solution.leftElement(A2, N2))  # Output: 4
