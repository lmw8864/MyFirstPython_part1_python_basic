# 5-1_2.py

"""
5-1. 조건 테스트
5-2. 더 많은 조건 테스트
"""

famous_constellations = ['Cassiopeia', 'Pegasus', 'Perseus', 'Hercules', 'Aquarius', 'Leo', 'Gemini', 'Capricornus']
my_constellation = 'capricornus'
print("Is my_constellation == 'gemini'?")
print(my_constellation == 'gemini')

print("\nIs my_constellation == 'capricornus'?")
print(my_constellation == 'capricornus')

print("\nIs my_constellation in famous_constellations?")
print(my_constellation in famous_constellations)

print("\nIs my_constellation.title() in famous_constellations?")
print(my_constellation.title() in famous_constellations)

print("\nIs my_constellation.title() not in famous_constellations?")
print(my_constellation.title() not in famous_constellations)

print("\nFamous constellations are here.")
for constellation in famous_constellations:
    print("\nIs " + constellation + " your constellation?")
    if constellation.lower() == my_constellation:
        print("Yes, " + constellation + " is my constellation!")
    else:
        print("No.")


members = ['Dongjin', 'Rancho', 'Minwoo']
print("\n'Dongjin' in members and 'Rancho' in members?")
result = 'Dongjin' in members and 'Rancho' in members
print(result)

print("\n'Jiho' in members and 'Rancho' in members?")
result = 'Jiho' in members and 'Rancho' in members
print(result)

print("\n'Jiho' in members or 'Rancho' in members?")
result = 'Jiho' in members or 'Rancho' in members
print(result)
