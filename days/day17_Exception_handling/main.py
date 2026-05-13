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
#Unpacking
def sum_of_five_nums(a, b, c, d, e):
    return a + b + c + d + e
lst = [1, 2, 3, 4, 5]
print(sum_of_five_nums(*lst)) #The * opens the list and spreads the values

numbers = range(2, 7)
print(list(numbers))
args = [2, 7]
numbers = range(*args)
print(numbers)

#Packing
def sum_all(*args):
    s = 0
    for i in args:
        s += i
    return s
print(sum_all(1, 2, 3))
print(sum_all(1, 2, 3, 4, 5, 6, 7))

#Spreading
lst_one = [1, 2, 3]
lst_two = [4, 5, 6, 7]
lst = [0, *lst_one, *lst_two]
print(lst) # [0, 1, 2, 3, 4, 5, 6, 7]

country_lst_one = ['Finland', 'Sweden', 'Norway']
country_lst_two = ['Algeria', 'France']
countries = [*country_lst_one, *country_lst_two]
print(countries)

