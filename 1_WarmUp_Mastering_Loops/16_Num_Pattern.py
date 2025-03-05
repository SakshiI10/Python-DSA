'''
1
2 3
4 5 6
7 8 9 10
11 12 13 14 15 '''

def print_patterns(n):
    sum=0
    for i in range(1, n+1):
        for j in range(1, i+1):
            sum += 1
            print(sum, end=" ")
        print()
       
n=5
print_patterns(n)