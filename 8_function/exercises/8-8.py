# 8-8.py

"""
8-8. 사용자 앨범
"""


def make_album(artist, title, count=''):
    dic_album = {'artist': artist.title(), 'title': title.title()}
    if count:
        dic_album['count'] = count
    return dic_album

print("\n앨범 정보를 입력하세요.")
print("(종료를 원하시면 'q'를 입력하세요.)")


all_albums = []
while True:
    artist = input("\n아티스트: ")
    if artist == 'q':
        break
    title =  input("앨범 제목: ")
    if title == 'q':
        break
    count = input("앨범 곡 수: ")
    if count == 'q':
        break

    print(artist.title() + "의 " + title.title() + ", 총 " + str(count) + "곡")
    print(make_album(artist, title, count))
    all_albums.append(make_album(artist, title, count))

for album in all_albums:
    print(album)

# 앨범 정보를 입력하세요.
# (종료를 원하시면 'q'를 입력하세요.)
#
# 아티스트: 에이핑크
# 앨범 제목: pink up
# 앨범 곡 수: 7
# 에이핑크의 Pink Up, 총 7곡
# {'title': 'Pink Up', 'count': '7', 'artist': '에이핑크'}
#
# 아티스트: 보아
# 앨범 제목: camo
# 앨범 곡 수: 1
# 보아의 Camo, 총 1곡
# {'title': 'Camo', 'count': '1', 'artist': '보아'}
#
# 아티스트: 헤이즈
# 앨범 제목: /// (너 먹구름 비)
# 앨범 곡 수: 5
# 헤이즈의 /// (너 먹구름 비), 총 5곡
# {'title': '/// (너 먹구름 비)', 'count': '5', 'artist': '헤이즈'}
#
# 아티스트: q
# {'title': 'Pink Up', 'count': '7', 'artist': '에이핑크'}
# {'title': 'Camo', 'count': '1', 'artist': '보아'}
# {'title': '/// (너 먹구름 비)', 'count': '5', 'artist': '헤이즈'}
