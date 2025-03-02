'''
*****
*****
*****
*****
***** '''

n=5

print("Using one loop: ")
# Using one loop
for i in range(n):
    print("*" * n)  # Print 5 stars in a single row

print("Using two loops: ")
# Using two loops
for i in range(n):
    for j in range(n):
        print('*', end="") 
    print()