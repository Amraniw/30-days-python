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
