# 6-11.py

"""
6-11. 도시
"""

cities = {
    'incheon': {
        'country': 'korea',
        'population': '2,925,815',
        'fact': '동진이 살아요~'
    },
    'seoul': {
        'country': 'korea',
        'population': '10,421,782',
        'fact': '민우 살아요~'
    },
    'bucheon': {
        'country': 'korea',
        'population': '869,743',
        'fact': '모르는 동네에요~'
    },
}

for city, city_info in cities.items():
    print("\nCity: " + city.title())
    for key, value in city_info.items():
        print(key.title() + ": " + value.title())



