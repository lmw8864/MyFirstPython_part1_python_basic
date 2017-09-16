# string.py

# 대소문자 바꾸기
name = "ada lovelace"
print(name.title())     # Ada Lovelace

name = " Ada lovelace"
print(name.upper())     # ADA LOVELACE
print(name.lower())     # ada lovelace

# 문자열 병합
first_name = "ada"
last_name = "lovelace"
full_name = first_name + " " + last_name

message = "Hello, " + full_name.title() + "!"
print(message)          # Hello, Ada Lovelace!

# 탭이나 줄바꿈 문자로 문자열에 공백 추가하기
print("Python")         # 'Python'
print("\tPython")       # '	Python'
print("Languages:\nPython\nC\nJavaScript")
# Languages:
# Python
# C
# JavaScript

print("Languages:\n\tPython\n\tC\n\tJavaScript")
# Languages:
# 	Python
# 	C
# 	JavaScript

# 공백 잘라내기
language = " python "
print(language)             # ' python '
print(language.rstrip())    # ' python'
print(language.lstrip())    # 'python '
print(language.strip())     # 'python'

# ※ 파이썬은 작은따옴표(')와 아포스트로피(`)를 구분하지 못한다. -> 그럼 큰따옴표(") 안에 쓰면 되잖아?
