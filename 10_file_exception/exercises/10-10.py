# 10-10.py

"""
10-10. 흔한 단어

count() 메서드를 써서 단어나 구절이 문자열에 몇 번 나타났는지 알아볼 수 있습니다.

예:
    line = "Row, row, row your boat"
    print(line.count('row'))  # 2

    # lower() 를 써서 문자열을 소문자로 바꾸면 대소문자와 상관없이 원하는 단어를 찾을 수 있습니다.
    print(line.lower().count('row'))  # 3
"""


def count(filename, word):
    """파일에 존재하는 단어 수를 셉니다."""
    try:
        with open(filename, 'r') as f:
            contents = f.read()
            num_word = contents.lower().count(word)
    except FileNotFoundError:
        print(filename + "파일이 존재하지 않습니다.")
    else:
        print(filename + "에 존재하는 '" + word + "'의 수는 " + str(num_word) + "개입니다.")

files = ['alice.txt', 'little_women.txt', 'love.txt', 'moby_dick.txt']
word = input("세고 싶은 단어: ")
for file in files:
    count(file, word)

# 세고 싶은 단어: love
# alice.txt에 존재하는 'love'의 수는 18개입니다.
# little_women.txt에 존재하는 'love'의 수는 466개입니다.
# love.txt파일이 존재하지 않습니다.
# moby_dick.txt에 존재하는 'love'의 수는 56개입니다.
