# 
# Vena
# Add two number then print the bigger number
#

# 1. Input
n1 = int(input('Number 1: '))
n2 = int(input('Number 2: '))

# 2. Process
if n1>n2:
    bigger = n1
elif n1<n2:
    bigger = n2
else:
    bigger = 'same'

# 3. Output
print(f'Bigger : {bigger}')