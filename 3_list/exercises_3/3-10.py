# 3-10.py

"""
3-10. 모든 함수
"""
anything = ['python', '제주도', '신동진', '노란초', 'Love']
print(anything)                     # ['python', '제주도', '신동진', '노란초', 'Love']
print(sorted(anything))             # ['Love', 'python', '노란초', '신동진', '제주도'] → 영대/영소/한글 순
print(sorted(anything, reverse=True))   # ['제주도', '신동진', '노란초', 'python', 'Love']
print(anything)                     # ['python', '제주도', '신동진', '노란초', 'Love'] → 리스트 순서는 그대로
anything.sort()
print(anything)                     # ['Love', 'python', '노란초', '신동진', '제주도'] → 리스트 순서 바뀜
anything.sort(reverse=True)
print(anything)                     # ['제주도', '신동진', '노란초', 'python', 'Love']

print('\n')
anything = ['python', '제주도', '신동진', '노란초', 'Love']
print(anything)                     # ['python', '제주도', '신동진', '노란초', 'Love']
anything.reverse()
print(anything)                     # ['Love', '노란초', '신동진', '제주도', 'python']
anything.reverse()
print(anything)                     # ['python', '제주도', '신동진', '노란초', 'Love'] → 원래 순서로 돌아옴

anything_length = len(anything)
print(anything_length)              # 5
