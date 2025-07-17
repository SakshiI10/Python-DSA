'''
Given a lowercase string array arr[]. Each element in the array represents a vote cast for a candidate. Return the name of the candidate who received the maximum number of votes and the count of votes he received. In case of a tie between two or more candidates, return the lexicographically smallest name.

Input: arr[] = ["john", "johnny", "jackie", "johnny", "john", "jackie", "jamie", "jamie", "john", "johnny", "jamie", "johnny", "john"]
Output: ["john", "4"]'''

class Solution:
    def winner(self, arr):
        freq = {}

        for name in arr:
            if name in freq:
                freq[name] += 1
            else:
                freq[name] = 1
        max_votes = max(freq.values())

        winners = []
        for name in freq:
            if freq[name] == max_votes:
                winners.append(name)
        winner_name = min(winners)

        return [winner_name, str(max_votes)]
    
sol = Solution()

arr = ["john", "johnny", "jackie", "johnny", "john", "jackie", "jamie", "jamie", "john", "johnny", "jamie", "johnny", "john"]
print(sol.winner(arr)) 

arr2 = ["andy", "blake", "clark"]
print(sol.winner(arr2)) 
