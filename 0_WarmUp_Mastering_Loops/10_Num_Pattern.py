'''
1
2 2 
3 3 3
4 4 4 4
5 5 5 5 5 '''

def print_pattern(n):
    for i in range(1, n+1):
        for j in range(i):
            print(i, end=" ")
        print()

n=5
print_pattern(n)