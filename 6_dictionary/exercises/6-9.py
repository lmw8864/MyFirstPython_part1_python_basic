# 6-9.py

"""
6-9. 좋아하는 장소
"""

favorite_places = {
    'eric': ['india', 'china', 'pairs'],
    'lucia': ['japan', 'hongkong'],
    'ronaldo': ['paris', 'spain'],
}

for name, places in favorite_places.items():
    print('\n' + name.title() + "'s favorite places:")
    for place in places:
        print(place.title())
