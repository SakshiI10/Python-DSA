'''
Geek is given a task to select at most 10 employees for a company project. Each employee is represented by a single-digit ID number which is unique for all the selected employees for the project. Geek has a technical problem in his system which printed ID number multiple times. You are given array arr having all printed IDs. Help him to get rid of the repeated IDs.

Input: arr[] = [8, 8, 6, 2, 1] 
Output: [8, 6, 2, 1] '''

class Solution:
    def uniqueId(self, arr):
        unique_elements = []
        n=len(arr)
        
        for i in range(n):
            if arr[i] not in unique_elements:  
                unique_elements.append(arr[i])

        return unique_elements
    
arr = [8, 8, 6, 2, 1]
sol = Solution()
print(sol.uniqueId(arr))  # Output: [8, 6, 2, 1]
