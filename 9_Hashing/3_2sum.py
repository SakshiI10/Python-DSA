class Solution():
    def twosum(self, arr, k):
        n=len(arr)
        hash_table={}

        for i in range(n):
            compliment=k-arr[i]
            if compliment in hash_table:
                return[hash_table[compliment], i]
            hash_table[arr[i]]=i

    def twosum2(self, arr, k):
        n = len(arr)
        hash_table = {}
        result = []

        for i in range(n):
            complement = k - arr[i]
            if complement in hash_table:
                for j in hash_table[complement]:
                    result.append([j, i])

            if arr[i] not in hash_table:
                hash_table[arr[i]] = []
            hash_table[arr[i]].append(i)

        return sorted(result)
                       
sol=Solution()
a = [10, 20, 30, 20, 10, 30]
k = 50
print(sol.twosum(a, k))
print(sol.twosum2(a, k))

# hash_table[compliment] is returning a list containing two indices: the index of the complement number (which was seen earlier and stored in the hash table), i — the index of the current number being checked.
