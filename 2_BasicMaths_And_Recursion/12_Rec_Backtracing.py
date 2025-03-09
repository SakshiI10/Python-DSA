# Print number from 1 to N using Backtracking.
def backtrack(i):
    if i == 0:
        return
    backtrack(i-1)
    print(i)

n=5
backtrack(n)

print()

# Print number from N to 1 using Backtracking.
def backtrack(i):
    if i == 0:
        return
    print(i)
    backtrack(i-1)

n=5
backtrack(n)
