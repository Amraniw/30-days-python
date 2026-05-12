# Declaring and Calling a Function
def generate_full_name():
    first_name = 'Wassim'
    last_name = 'Amrani'
    space = ' '
    full_name = first_name + space + last_name
    return full_name 
print(generate_full_name())

def add_two_numbers():
    number_one = 2
    number_two = 3
    total = number_one + number_two
    return total
print(add_two_numbers())

# Function with Parameters
def add_ten(num):
    ten = 10
    return num + ten
print(add_ten(90))

def square_number(x):
    return x * x
print(square_number(4))

def calculate_age(current_year, birth_year):
    age = current_year - birth_year
    return age
print('Age:', calculate_age(2026, 2003))

def add_two_numbers(num1, num2):
    total = num1 + num2
    return total
print(add_two_numbers(3, 5))

def generate_full_name (first_name = 'Wassim', last_name = 'Amrani'):
    space = ' '
    full_name = first_name + space + last_name
    return full_name

print(generate_full_name())
print(generate_full_name('David','Smith'))

def weight_of_object(mass, gravity = 9.81):
    weight = str(mass * gravity)+ ' N'
    return weight
print('Weight of an object in Newtons:', weight_of_object(100))
print('Weight of an object in Newtons:', weight_of_object(100, 1.62))

# Arbitrary Number of Arguments
def sum_all_nums(*nums):
    total = 0
    for num in nums:
        total += num  # same total = total + num
    return total
print(sum_all_nums(2, 3, 5))