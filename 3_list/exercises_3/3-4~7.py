# 3-4_5_6_7.py

"""
3-4. 손님 리스트
3-5. 손님 리스트 바꾸기
3-6. 더 많은 손님
3-7. 손님 리스트 줄이기
"""
invite_dinner = ['동진', '란초', '형래']
message = '님, 저녁식사에 초대합니다. "같이 밥 먹어요!"'
print(invite_dinner[0] + message)
print(invite_dinner[1] + message)
print(invite_dinner[2] + message)

# 손님 리스트 바꾸기
print(invite_dinner[1] + "님께서 바빠서 불참하신다고 합니다.")
invite_dinner[1] = '신율'

for name in invite_dinner:
    print(name + message)

# 손님 리스트 늘리기
print("※공지: 더 큰 저녁식탁을 발견했어요! 몇 명 더 초대할게요!")
invite_dinner.insert(0, '돌아온 형래')
invite_dinner.insert(3, '지호')
invite_dinner.append('형래의 행복(wife)')

for name in invite_dinner:
    print(name + message)

# 손님 리스트 줄이기
print("※공지: 사정이 생겨서 두 분 밖에 초대할 수가 없게 되었습니다. 다른 분들은 다음에 다시 초대할게요ㅠ")
message_out = "님, 죄송합니다. 다음 기회에 꼭 함께해요!"
# popped_name = invite_dinner.pop()
# print(popped_name + message_out)
# popped_name = invite_dinner.pop()
# print(popped_name + message_out)
# popped_name = invite_dinner.pop()
# print(popped_name + message_out)
# popped_name = invite_dinner.pop()
# print(popped_name + message_out)
# print(invite_dinner)

while len(invite_dinner) > 2:
    popped_name = invite_dinner.pop()
    print(popped_name + message_out)
    print(invite_dinner)

message_in = "님에 대한 저녁식사 초대는 유효합니다. 우리끼리 밥 먹어요!"
for name in invite_dinner:
    print(name + message_in)

# 리스트 항목 제거, 빈 리스트 만들기
# del invite_dinner[0]
# print(invite_dinner)
# del invite_dinner[0]
# print(invite_dinner)

while len(invite_dinner) >= 1:
    del invite_dinner[0]
    print(invite_dinner)
