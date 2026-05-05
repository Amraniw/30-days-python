print('Division: ', 6 / 2)  #Division in Python gives floating number - 2.0

print('Division: ', 7 // 3) # // gives floor division

print('Modulus: ', 3 % 2) 

print('Exponentiation: ', 2 ** 3) # 2^3

print('Multiplying complex numbers: ',(1 + 1j) * (1 - 1j)) # multiplying complex numbers


#Area of circle
radius = 10
area_of_circle = 3.14 * radius ** 2
print('Area of a circle: ', area_of_circle)

#Area of a rectangle
length = 10
width = 20
area_of_rectangle = length * width
print('Area of a rectangle: ', area_of_rectangle)

#Weight of an object
mass = 75 #kg
gravity = 9.81
weight = mass * gravity
print('Weight of an object: ', weight, 'N')

#Density of a liquid
mass = 75 #kg
volume = 0.075 # in cubic meter
density = mass/volume
print('Density of a liquid', density, "kg/m^3")


# Comparison Operators

print(len('mango') == len('avocado'))
print(len('mango') != len('avocado'))
print(len('mango') < len('avocado'))

print('1 is 1', 1 is 1 )
print('1 is not 2', 1 is not 2)
print('coding' in 'coding for all')
print('s' in 'Wassim')
print('R' not in 'Ronaldo')

#Logical Operators

print(not True)
print(not False)
print(not not True)
print( 3 < 2 and 4 > 3)
print( 3 < 2 or 4 > 3)

#Exercise

age = 22
height = 1.83
complex_number = 1 + 3j

# area of a triangle as an input
base = float(input('Enter base: '))
height = float(input('Eneter height: '))
area_triangle = 0.5 * base * height
print('The area of the triangle is: ', area_triangle)
