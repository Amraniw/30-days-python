try:
    print(10 + '5')
except:
    print('something went wrong')


try:
    name = input('Enter your name:')
    year_born = int(input('Year you were born:'))
    age = 2026 - year_born
    print(f'You are {name}, and your age is {age}.')
except:
    print('Something went wrong')

# year_born has to be int because if not, in the next line, we are substracting a int with a string and that causes an error


