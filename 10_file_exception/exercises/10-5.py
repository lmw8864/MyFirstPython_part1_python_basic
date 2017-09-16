# 10-5.py

"""
10-5. 프로그래밍 투표
"""

while True:
    reason = input("당신이 프로그래밍을 좋아하는 이유는 무엇인가요? (종료하시려면 'q' 입력): ")
    if reason == 'q':
        break
    with open('reasons.txt', 'a') as f:
        f.write(reason + "\n")
