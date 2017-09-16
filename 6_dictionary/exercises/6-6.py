# 6-6.py

"""
6-6. 설문
"""

favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}

users = ['michel', 'phil', 'leechze', 'aromi', 'sarah']

for user in users:
    if user in favorite_languages.keys():
        print(user.title() + ", thank you for taking the poll.")
    else:
        print(user.title() + ", please take our poll.")
