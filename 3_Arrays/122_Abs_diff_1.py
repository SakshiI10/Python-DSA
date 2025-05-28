'''
Given an array arr. Return all the numbers less than k and the number which have at least two digits and the absolute difference between every adjacent digit of that number should be 1 in the array.

Input: arr[] = [7, 98, 56, 43, 45, 23, 12, 8], k = 54
Output: [43, 45, 23, 12]'''

class Solution:
    def getDigitDiff1AndLessK(self, arr, k):
        res=[]
        
        for num in arr:
            if num<k and num>=10:
                digits = list(str(num))
                valid=True
                
                for i in range(len(digits)-1):
                    if abs(int(digits[i]) - int(digits[i+1])) != 1:
                        valid = False
                        break
                if valid:
                    res.append(num)
        return res
    
sol=Solution()
arr=[7, 98, 56, 43, 45, 23, 12, 8]
k = 54
print(sol.getDigitDiff1AndLessK(arr, k)) 
