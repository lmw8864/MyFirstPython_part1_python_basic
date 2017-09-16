# 6-7.py

"""
6-7. 사람들
"""
people = []

user = {
    'first_name': 'dongjin',
    'last_name': 'shin',
    'age': 33,
    'city': 'inchon',
}
people.append(user)

user = {
    'first_name': 'rancho',
    'last_name': 'noh',
    'age': 33,
    'city': 'inchon',
}
people.append(user)

user = {
    'first_name': 'minwoo',
    'last_name': 'lee',
    'age': 33,
    'city': 'seoul',
}
people.append(user)

for user in people:
    full_name = user['last_name'].title() + " " + user['first_name'].title()
    age = str(user['age'])
    city = user['city'].title()

    print(full_name + " is " + age + " years old and lives in " + city + ".")
