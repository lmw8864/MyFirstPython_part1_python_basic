# 8-6.py

"""
8-6. 도시 이름
"""
def city_country(city, country):
    city_country = {'city': city, 'country': country}
    result = '"' + city_country['city'].title() + ', ' + city_country['country'].title() + '"'
    return result

print(city_country('santiago', 'chile'))
print(city_country('seoul', 'korea'))
print(city_country('paris', 'france'))
