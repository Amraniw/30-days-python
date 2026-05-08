# 2 ways to create a list
lst = list()
print(len(lst))

lst = []
print(len(lst))

#list with initail values

web_techs = ['HTML', 'CSS', 'JS', 'React', 'Redux', 'Node', 'MongDB']
print('Web technologies:', web_techs)
print('Number of web technologies: ', len(web_techs))

#Unpacking List Items
lst = ['item1', 'item2', 'item3', 'item4', 'item5']
first_item, second_item, third_item, *rest = lst
print(first_item)
print(second_item)
print(third_item)
print(rest)

#slicing
fruits = ['banana', 'orange', 'mango', 'lemon']
orange_and_mango = fruits[1:3] #does not include index 3
print(orange_and_mango)

#modifying a list
fruits = ['banana', 'orange', 'mango', 'lemon']
fruits[0] = 'apple'
print(fruits)

#Checking Items in a List
fruits = ['banana', 'orange', 'mango', 'lemon']
does_exist = 'banana' in fruits
print(does_exist)

#Adding Items to a List
fruits = ['banana', 'orange', 'mango', 'lemon']
fruits.append('apple') #append only takes 1 argument
print(fruits)

#Inserting and removing Items into a List
fruits = ['banana', 'orange', 'mango', 'lemon']
fruits.insert(2, 'apple') # lst.insert(index, item)
fruits.remove('banana') # lst.remove(item)
print(fruits)