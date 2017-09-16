# 9-4.py

"""
9-4. 고객 숫자
"""


class Restaurant():
    """레스토랑을 모델화"""
    def __init__(self, restaurant_name, cuisine_type):
        """속성 초기화"""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0  # 기본값 0

    def describe_restaurant(self):
        """레스토랑 정보를 출력합니다."""
        print("\n레스토랑 이름: " + self.restaurant_name.title())
        print("음식 타입: " + self.cuisine_type.title())

    def open_restaurant(self):
        """레스토랑 오픈 메시지 출력"""
        print("\n" + self.restaurant_name + "이 오픈했습니다. 많은 관심 부탁드립니다!")

    # 서빙한 고객 숫자를 지정하는 메서드 추가
    def set_number_served(self, number):
        """서빙한 고객 숫자를 지정합니다."""
        self.number_served = number

    # 서빙한 고객 숫자를 지정한 값만큼 늘리는 메서드 추가
    def increment_number_served(self, number):
        """서빙한 고객 숫자를 지정한 값만큼 늘립니다."""
        self.number_served += number


# 인스턴스 생성
mad_for_garlic = Restaurant('mad for garlic', 'italian')
print("서빙한 고객 숫자: " + str(mad_for_garlic.number_served))

# 속성값 바꾸기 (인스턴스에서 직접 접근)
mad_for_garlic.number_served = 17
print("서빙한 고객 숫자: " + str(mad_for_garlic.number_served))

# 속성값 바꾸기 (메서드를 통해서 바꾸기)
mad_for_garlic.set_number_served(20000)  # 20000 지정
print("서빙한 고객 숫자: " + str(mad_for_garlic.number_served))

# 속성값 늘리기
mad_for_garlic.increment_number_served(100)  # 100 추가
print("서빙한 고객 숫자: " + str(mad_for_garlic.number_served))
