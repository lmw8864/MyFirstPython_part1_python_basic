# 8-7.py

"""
8-7. 앨범
"""
def make_album(artist, title, count=''):
    dic_album = {'artist': artist, 'title': title}
    if count:
        dic_album['count'] = count
    return dic_album

print(make_album('Apink', 'Pink UP', count=7))
print(make_album('BoA', 'CAMO'))
print(make_album('Heize', '/// (너 먹구름 비)', 5))
