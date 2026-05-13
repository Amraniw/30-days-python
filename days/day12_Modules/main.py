#importing a module 
import mymodule
print(mymodule.generate_full_name('Wassim', 'Amrani'))

import string
print(string.ascii_letters)
print(string.digits)
print(string.punctuation)

from random import random, randint
print(random()) #prints a number between 0 and 0.9999
print(randint(5, 20)) #prints a random number as integer between 5 and 20
