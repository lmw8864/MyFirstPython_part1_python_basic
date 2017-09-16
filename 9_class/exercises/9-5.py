# 9-5.py

"""
9-5. 로그인 시도
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
        self.attempts = 0  # 로그인 시도 횟수 속성 추가

    def describe_user(self):
        """사용자 정보 출력"""
        print("\n이름: " + self.full_name)
        print("나이: " + str(self.age))
        print("주소: " + self.address)

    def greet_user(self):
        """환영 인사 메시지"""
        print(self.full_name + "님, 환영합니다!")

    # 로그인 시도 횟수를 1씩 늘리는 메서드 추가
    def increment_login_attempts(self):
        """로그인 시도 횟수를 1 증가시킵니다."""
        self.attempts += 1

    # 로그인 시도 횟수를 0으로 리셋하는 메서드 추가
    def reset_login_attempts(self):
        """로그인 시도 횟수를 0으로 리셋합니다."""
        self.attempts = 0
        print(self.full_name + "님의 로그인 시도 횟수가 리셋되었습니다.")

    def show_login_attempts(self):
        """로그인 시도 횟수를 보여줍니다."""
        print(self.full_name + "님의 로그인 시도 횟수는 " + str(self.attempts) + "회입니다.")

# 인스턴스 생성
djshin = User('dongjin', 'shin', 33, '인천')

# 로그인 5번 시도
djshin.increment_login_attempts()
djshin.increment_login_attempts()
djshin.increment_login_attempts()
djshin.increment_login_attempts()
djshin.increment_login_attempts()

# 로그인 시도 횟수 출력
djshin.show_login_attempts()

# 로그인 시도 횟수 리셋
djshin.reset_login_attempts()
djshin.show_login_attempts()
