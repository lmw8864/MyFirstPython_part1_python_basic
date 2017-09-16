# 5-11.py

"""
5-11. 순번
"""

numbers = [number for number in range(1, 10)]
# print(numbers)
for number in numbers:
    if number == 1:
        result = str(number) + 'st'
    elif number == 2:
        result = str(number) + 'nd'
    elif number == 3:
        result = str(number) + 'rd'
    else:
        result = str(number) + 'th'
    print(result)
