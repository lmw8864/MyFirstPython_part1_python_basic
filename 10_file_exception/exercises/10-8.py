# 10-8.py

"""
10-8. 고양이와 개
"""


def show_contents(filename):
    """파일의 내용을 보여줍니다."""
    try:
        with open(filename, 'r') as f:
            contents = f.read()
    except FileNotFoundError:
        print(filename + " 파일이 존재하지 않습니다.")
    else:
        print(contents)

show_contents('cats.txt')
show_contents('dogs.txt')

# 미옹
# 코코
# 전하
# dogs.txt 파일이 존재하지 않습니다.
