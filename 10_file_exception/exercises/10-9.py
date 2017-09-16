# 10-9.py

"""
10-9. 조용한 개와 고양이
"""

def show_contents(filename):
    """파일의 내용을 보여줍니다."""
    try:
        with open(filename, 'r') as f:
            contents = f.read()
    except FileNotFoundError:
        pass  # 파일이 존재하지 않으면 아무것도 하지 않음
    else:
        print(contents)

show_contents('cats.txt')
show_contents('dogs.txt')

# 미옹
# 코코
# 전하
