a = 3
if a < 0:
    print('A is a negative number')
elif a > 0:
    print('A is a positive number')
else: 
    print('A is equal to 0')

#Nested conditions 
a = 0
if a > 0:
    if a % 2:
        print('A is positive and even integer')
    else:
        print('A is a positive integer')
elif a == 0:
    print('A is zero')
else:
    print('A is a negative number')
