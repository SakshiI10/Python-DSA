class Solution():
    def twosum(self, arr, k):
        hash_table={}
        n=len(arr)

        for i in range(n):
            compliment=k-arr[i]
            if compliment in hash_table:
                return[hash_table[compliment], i]
            hash_table[arr[i]]=i
                       
sol=Solution()
a = [2, 6, 5, 8, 11]
k = 10
len1 = sol.twosum(a, k)
print(len1)

# hash_table[compliment] is returning a list containing two indices: the index of the complement number (which was seen earlier and stored in the hash table), i — the index of the current number being checked.

