'''
1 2 3 4 5 
1 2 3 4
1 2 3
1 2
1 '''

def print_pattern(n):
    for i in range(n+1, 1, -1):
        for j in range(1, i):
            print(j, end=" ")
        print()

n=6
print_pattern(n)