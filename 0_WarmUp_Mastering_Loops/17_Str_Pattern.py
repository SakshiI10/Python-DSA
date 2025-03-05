'''
A
AB
ABC
ABCD
ABCDE'''

def print_pattern(n):
    for i in range(n): 
        for j in range(i + 1): 
            print(chr(65 + j), end="") 
        print()  

n = 5
print_pattern(n)
