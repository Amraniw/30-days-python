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
    if a % 2 == 0:
        print('A is positive and even integer')
    else:
        print('A is a positive integer')
elif a == 0:
    print('A is zero')
else:
    print('A is a negative number')

#If Condition and Logical Operators
a = 5
if a > 0 and a % 2 == 0:
    print('A is a positive and even integer')
elif a > 0 and a & 2 != 0:
    print('A is a positive integer')
elif a == 0:
    print('A is equal to 0')
else:
    print('A is negative')

# If and Or Logical Operators
user = 'James'
access_level = 3
if user == 'admin' or access_level >= 4:
    print('Access granted!')
else:
    print('Access denied!')