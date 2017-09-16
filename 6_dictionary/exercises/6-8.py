# 6-8.py

"""
6-8. 애완동물
"""
pets = []

pet = {
    'name': 'koko',
    'animal_type': 'cat',
    'owner': 'aromi',
}
pets.append(pet)

pet = {
    'name': 'roly',
    'animal_type': 'dog',
    'owner': 'michel',
}
pets.append(pet)

pet = {
    'name': 'miong',
    'animal_type': 'cat',
    'owner': 'aromi'
}
pets.append(pet)

for pet in pets:
    name = pet['name'].title()
    animal_type = pet['animal_type']
    owner = pet['owner'].title()

    print(owner + "`s " + animal_type + " is " + name + ".")
