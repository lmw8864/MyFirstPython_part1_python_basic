# 9-3.py

"""
9-3. 사용자
"""


class User():
    """사용자 프로필"""
    def __init__(self, first_name, last_name, age, address):
        """속성 초기화"""
        self.first_name = first_name
        self.last_name = last_name
        self.full_name = self.first_name.title() + " " + self.last_name.title()
        self.age = age
        self.address = address

    def describe_user(self):
        """사용자 정보 출력"""
        print("\n이름: " + self.full_name)
        print("나이: " + str(self.age))
        print("주소: " + self.address)

    def greet_user(self):
        """환영 인사 메시지"""
        print(self.full_name + "님, 환영합니다!")


# 인스턴스 생성
mwlee = User('minwoo', 'lee', 33, '서울')
djshin = User('dongjin', 'shin', 33, '인천')
rcnoh = User('rancho', 'noh', 33, '인천')

# 메서드 호출
mwlee.describe_user()
mwlee.greet_user()

djshin.describe_user()
djshin.greet_user()

rcnoh.describe_user()
rcnoh.greet_user()
