'''
1      1
12    21 
123  321
12344321 '''

def print_patterns(n):
    for i in range(1, n+1):
        for j in range(1, i+1):
            print(j, end="")
        
        for j in range(2*(n-i)):
            print(" ",end="")

        for j in range(i, 0, -1):
            print(j, end="")
        
        print()
       
n=4
print_patterns(n)