'''
1 2 3 4 5 
1 2 3 4
1 2 3
1 2
1 '''

def print_pattern(n):
    for i in range(n+1, 0, -1):
        for j in range(1, i):
            print(j, end=" ")
        print()

n=5
print_pattern(n)