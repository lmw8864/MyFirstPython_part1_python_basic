# 6-4.py

"""
6-4. 용어 사전 2
"""
programming_dic = {
    'list': '순서가 있는 모음',
    'dictionary': '키-값 쌍의 모음',
    'loop': '반복',
    'boolean': 'True or False',
}

for word, meaning in programming_dic.items():
    print("word: " + word)
    print("meaning: " + meaning + "\n")

# 단어 추가
programming_dic['items() 메서드'] = '키-값 쌍 리스트를 반환'
programming_dic['keys() 메서드'] = '키를 리스트로 반환'
programming_dic['values() 메서드'] = '값을 리스트로 반환'
programming_dic['sorted() 함수'] = '정렬(임시)'
programming_dic['set() 함수'] = '중복을 제거한 리스트를 반환'

print("\n※ 단어가 추가되었습니다.")

for word, meaning in programming_dic.items():
    print("word: " + word)
    print("meaning: " + meaning + "\n")

# ※ 단어가 추가되었습니다.
# word: set() 함수
# meaning: 중복을 제거한 리스트를 반환
#
# word: sorted() 함수
# meaning: 정렬(임시)
#
# word: loop
# meaning: 반복
#
# word: boolean
# meaning: True or False
#
# word: values() 메서드
# meaning: 값을 리스트로 반환
#
# word: keys() 메서드
# meaning: 키를 리스트로 반환
#
# word: list
# meaning: 순서가 있는 모음
#
# word: items() 메서드
# meaning: 키-값 쌍 리스트를 반환
#
# word: dictionary
# meaning: 키-값 쌍의 모음
