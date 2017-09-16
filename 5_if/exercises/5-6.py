# 5-6.py

"""
5-6. 성장단계
"""

age = 33

if age < 2:
    result = 'baby'
elif age < 4:
    result = 'toddler'
elif age < 13:
    result = 'kids'
elif age < 20:
    result = 'teenager'
elif age < 65:
    result = 'adult'
else:
    result = 'elder'

print(result)
