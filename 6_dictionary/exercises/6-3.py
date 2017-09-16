# 6-3.py

"""
6-3. 용어 사전
"""

programming_dic = {
    'list': '순서가 있는 모음',
    'dictionary': '키-값 쌍의 모음',
    'loop': '반복',
    'boolean': 'True or False',
}

print("list: " + programming_dic['list'] + "\n")
print("dictionary: " + programming_dic['dictionary'] + "\n")
print("loop: " + programming_dic['loop'] + "\n")
print("boolean: " + programming_dic['boolean'] + "\n")


# key 리스트 가져오기 (keys)
# https://wikidocs.net/16

print(programming_dic.keys())  # dict_keys(['dictionary', 'loop', 'boolean', 'list'])

for key in programming_dic.keys():
    print(key)
# list
# dictionary
# boolean
# loop

"""
dict_keys, dict_values, dict_items 등은 리스트로 변환하지 않더라도 
기본적인 반복성(iterate) 구문(예: for문)들을 실행할 수 있다.
"""

# dict_keys 객체를 리스트로 변환
keys = list(programming_dic.keys())
print(keys)  # ['dictionary', 'loop', 'boolean', 'list']

for key in keys:
    print(key)
# list
# dictionary
# boolean
# loop
