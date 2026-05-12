#While loop
count = 0
while count < 5:
    print(count)
    count = count + 1
else:
    print(count)

# Break and Continue 
count = 0
while count <5:
    print(count)
    count = count + 1
    if count == 3:
        break  #only prints 0 1 2

count = 0
while count < 5:
    if count == 3:
        count += 1
        continue
    print(count)
    count = count + 1 #Prints 0 1 2 4

# For loop
numbers = [0, 1, 2, 3, 4, 5]
for number in numbers: #number is a temporary name to refer to items in the list
    print(number)

language = 'Python'
for letter in language:
    print(letter)

# Break and Continue pt.2
numbers = (0, 1, 2, 3, 4, 5)
for number in numbers:
    print(number)
    if number ==3:
        break

numbers = (0, 1, 2, 3, 4, 5)
for number in numbers:
    print(number)
    if number ==3:
        continue
    print('Next number should be ', number + 1) if number != 5 else print("loop's end")

# Range function
for number in range(11):
    print(number)

# Nested for loop
person = {
    'first_name': 'Wassim',
    'last_name': 'Amrani',
    'age': 250,
    'country': 'Finland',
    'is_marred': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
}

for key in person:
    if key == 'skills':
        for skill in person['skills']:
            print(skill)

#For Else
for number in range(11):
    print(number)
else:
    print('The loop stops at', number)