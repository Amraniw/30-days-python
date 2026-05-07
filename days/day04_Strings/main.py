#multiline_string
multiline_string = """dsskdewkkkkkkkkkkkkkk
rewwwwwwwwwwwwwwwwwwwww
ewfdgggggggggggggggggggg"""
print(multiline_string)

#string concatenation  
first_name = "Ctistiano"
last_name = "Ronaldo"
space = ' '
full_name = first_name + space + last_name
print(full_name)

print('Hello big dawg. \nHow are you?')
print('Days\tTopics\tExercises')
print('Day 1\t5\t5')
print('Day 2\t6\t4')
print('Day 3\t5\t8')
print('Day 4\t2\t7')
print('This is a backlash symbol (\\)')
print('Every programming language starts with \'Hello Wold!\'')

#string formatting - %s = string
# %d = integers
# %f = floating point numbers
first_name = 'Wassim'
last_name = 'Amrani'
language = 'Python'
formated_string = 'I am %s %s. I teach %s' %(first_name, last_name, language)

radius = 10
pi = 3.14
area = pi * radius ** 2
formated_string = 'The area of a circle with a radius %d is %.2f.' %(radius, area) # 2 refers to 2 significant digits after the point
