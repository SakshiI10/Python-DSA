'''
E
D E
C D E
B C D E
A B C D E'''

def print_pattern(n):
    for i in range(n):
        char = 65 + n - 1 - i
        for j in range(i+1):
            print(chr(char+j), end="")
        print()

n=5
print_pattern(n)