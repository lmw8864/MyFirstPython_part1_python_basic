# 10-1.py

"""
10-1. 파이썬 배우기
"""

# 파일 전체 출력
with open('learning_python.txt') as f:
    contents = f.read()
    print(contents)


print("\n")
# 파일 객체에 루프를 실행하는 방법
with open('learning_python.txt') as f:
    for line in f:
        print(line.strip())


print("\n")
# 리스트에 저장하고 with 블록 밖에서 출력하는 방법
with open('learning_python.txt') as f:
    lines = f.readlines()

for line in lines:
    print(line.strip())
