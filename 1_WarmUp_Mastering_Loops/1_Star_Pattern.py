'''
*****
*****
*****
*****
***** '''

def pattern_using_single_loop(n):
    for i in range(n):
        print("*" * n)

def pattern_using_nested_loops(n):
    for i in range(n):
        for j in range(n):
            print('*', end="")
        print() 

n = 5
pattern_using_single_loop(n)
print()
pattern_using_nested_loops(n)
