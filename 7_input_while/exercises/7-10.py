# 7-10.py

"""
7-10. 꿈같은 휴가
"""

poll_dic = {}

while True:
    name = input("\n성함을 입력해주세요. : ")
    place = input("당신이 꿈꾸는 최고의 휴가지는 어디인가요? : ")

    poll_dic[name] = place

    repeat = input("\n설문에 참여하실 분이 또 계신가요? (Y/N): ")
    if repeat == 'N' or repeat == 'n':
        break
    elif repeat == 'Y' or repeat == 'y':
        continue
    else:
        print("잘못 입력하셨습니다. 처음으로 돌아갑니다.(입력하신 정보는 저장되었습니다)")

print("\n참여하신 설문 결과:")
for name, place in poll_dic.items():
    print("\t" + name.title() + '님의 최고의 휴가지는 ' + place + "입니다.")
