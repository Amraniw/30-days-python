# Built in functions 

print(len("Ronaldo"))
print(str(10))
print(int("10"))
print(float("10"))
print(help(str))

# Variables

first_name = 'Wassim'
last_name = 'Amrani'
country = 'Canada'
city = 'Montreal'
age = '22'
is_married = False
##person_info = {
    #'firstname' : 'Wassim',
   # 'lastname' : "Amrani",
  #  "country" : "Canada",
  #  "city" : "Montreak"

#}

# Declaring Multiple Variable in a Line

first_name, last_name, country, age, is_married = "Wassim", 'Amrani', 'Canada', '22', 'False'

print(first_name, last_name, country, age, is_married)
print('First name:', first_name)
print('Last name:', last_name)
print('Country:', country)
print('Age:', age)
print('Married:', is_married)


#int to float
num_int = 10
print('num_int', num_int)
num_float = float(num_int)
print('num_float:', num_float)

# float to int
gravity = 9.81
print(int(gravity))

# int to str
num_int = 10
print(num_int)
num_str = str(num_int)
print(num_str)

# str to int or float
num_str = '10.6'
num_float = float(num_str)
num_int = int(num_float)
print('num_str:', num_str)
print('num_float:', num_float)
print('num_int', num_int)

# str to list
first_name ='Wassim'
print(first_name)
first_name_to_list = list(first_name)
print(first_name_to_list)