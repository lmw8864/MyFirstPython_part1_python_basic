# 6-5.py

"""
6-5. 강
"""

rivers = {
    'nile': 'egypt',
    'mississippi': 'usa',
    'han': 'korea',
}

for river, country in rivers.items():
    if country == 'usa':
        print(river.title() + "강은 " + country.upper() + "에 있습니다.")
    else:
        print(river.title() + "강은 " + country.title() + "에 있습니다.")

print("\n")
# 각 강이름만 출력
for river in rivers.keys():
    print(river)

print("\n")
# 각 나라이름만 출력
for country in rivers.values():
    print(country)
