'''
4 4 4 4 4 4 4
4 3 3 3 3 3 4
4 3 2 2 2 3 4
4 3 2 1 2 3 4
4 3 2 2 2 3 4
4 3 3 3 3 3 4
4 4 4 4 4 4 4'''

def print_pattern(n):
    for i in range(n):
        for j in range(n):
            value = (n // 2) - min(i, j, n - i - 1, n - j - 1) + 1
            print(value, end=" ")
        print()  

n = 7
print_pattern(n)
