# 10-2.py

"""
10-2. C 배우기

    replace() 메서드를 써서 문자열의 단어를 다른 단어로 교체할 수 있습니다.
    - 예:
        message = "I really like dogs."
        message2 = message.replace("dog", "cat")

        print(message)  # I really like dogs.
        print(message2)  # I really like cats.
"""

# learning_python.txt 내용 확인
with open('learning_python.txt') as f:
    contents = f.read()
    print(contents)

# In Python you can store as much information as you want.
# In Python you can connect pieces of information.
# In Python you can model real-world situations.


print("\n")
# with 블록 안에서 작업
with open('learning_python.txt') as f:
    for line in f:
        line = line.replace('Python', 'C')
        print(line.rstrip())

# In C you can store as much information as you want.
# In C you can connect pieces of information.
# In C you can model real-world situations.


print("\n")
# 리스트로 저장하고 with 블록 밖에서 작업
with open('learning_python.txt') as f:
    lines = f.readlines()

for line in lines:
    line = line.replace('Python', 'C')
    print(line.rstrip())

# In C you can store as much information as you want.
# In C you can connect pieces of information.
# In C you can model real-world situations.
