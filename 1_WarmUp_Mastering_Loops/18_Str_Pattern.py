'''
ABCDE 
ABCD
ABC
AB
A '''

def print_pattern(n):
    for i in range(n, 0, -1): 
        for j in range(i): 
            print(chr(65 + j), end="") 
        print()  

n = 5
print_pattern(n)
