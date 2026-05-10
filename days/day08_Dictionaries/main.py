person = {
    'first_name':'Lamine',
    'last_name':'Yamal',
    'age':'18',
    'country':'Algeria',
    'is_married':False,
    'skills':['dribbling', 'vista', 'shooting', 'speed'],
    'adress':{
        'street':'Space street',
        'zipcode':'02210'
    }

}
print(len(person))

#Accessing Dictionnary items 
print(person['first_name'])
print(person['last_name'])
print(person['skills'])
print(person['skills'][1])
print(person['adress']['street'])


#Adding items 
person['Job_title'] = 'Footballer'
person['skills'].append('passes')
print(person)

#Removing 
person.pop('first_name')        # Removes the firstname item
person.popitem()                # Removes the address item
del person['is_married']        # Removes the is_married item

print(person.items())