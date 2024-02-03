# name = "Hamada"
# age = 41
# money = 800.20
# happy = True

person = ["Hamada", 41, 800.20, True]

# dictionary (hash table)

persons = [{'name': 'Hamada', 'age': 41, 'money': 800.20, 'happy': True}, 
            {'name': 'Mohamed', 'age': 35, 'money': 4000, 'happy': False},
            {'name': 'Amira', 'age': 38, 'money': 2000, 'happy': True}]

for index in range(0, len(persons)):
    print(persons[index]['name'])

# you can change the person to 0, 1, 2 etc. to choose which person you want information about
# you can change the input to 'name', 'age', 'money', 'happy' etc.
#print(persons[0]['age'])