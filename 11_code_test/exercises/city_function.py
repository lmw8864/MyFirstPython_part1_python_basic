# city_function.py


def city(city, country, population=''):
    if population:
        city_country = "City: " + city.title() + "\nCountry: " + country.title() + "\nPopulation: " + str(population)
    else:
        city_country = "City: " + city.title() + "\nCountry: " + country.title()
    return city_country

# print(city('santiago', 'chile'))
# print(city('santiago', 'chile', 5000000))
