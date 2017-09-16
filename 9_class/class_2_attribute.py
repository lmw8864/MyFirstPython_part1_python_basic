# class_2_attribute.py

"""
클래스와 인스턴스 다루기

 - 속성의 기본값 설정
 - 속성값을 바꾸는 3가지 방법
        - 인스턴스에서 값을 직접 바꾸기
        - 메서드를 통해 속성값 바꾸기
        - 메서드를 통해 속성값을 정해진 만큼씩만 바꾸기
"""


# Car 클래스
class Car():
    """자동차를 나타내는 코드"""

    def __init__(self, make, model, year):
        """자동차를 나타내는 속성 초기화"""
        self.make = make
        self.model = model
        self.year = year

    def get_descriptive_name(self):
        """알아보기 쉬운 이름 변환"""
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()

# 인스턴스 생성
my_new_car = Car('audi', 'a4', 2016)
print(my_new_car.get_descriptive_name())
# 2016 audi A4


# 속성의 기본값 설정
# 기본값을 설정할 때는 그 값을 __init__() 메서드 안에 넣어두는 게 합리적

class Car():
    """자동차를 나타내는 코드"""

    def __init__(self, make, model, year):
        """자동차를 나타내는 속성 초기화"""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0  # 자동차의 주행거리 속성 추가 및 기본값 설정

    def get_descriptive_name(self):
        """알아보기 쉬운 이름 변환"""
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()

    # 자동차의 주행거리 표시기를 읽기 쉽게 하는 메서드 추가
    def read_odometer(self):
        """주행거리를 나타내는 문장을 출력합니다."""
        print("This car has " + str(self.odometer_reading) + " miles on it.")

# 메서드 호출
my_new_car = Car('audi', 'a4', 2016)
print(my_new_car.get_descriptive_name())  # 2016 audi A4
my_new_car.read_odometer()
# This car has 0 miles on it.


print("\n")
# 속성값 바꾸기

# 인스턴스에서 값을 직접 바꾸기
my_new_car.odometer_reading = 23
my_new_car.read_odometer()
# This car has 23 miles on it.


# 메서드를 통해 속성값 바꾸기
class Car():
    """자동차를 나타내는 코드"""

    def __init__(self, make, model, year):
        """자동차를 나타내는 속성 초기화"""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """알아보기 쉬운 이름 변환"""
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()

    def read_odometer(self):
        """주행거리를 나타내는 문장을 출력합니다."""
        print("This car has " + str(self.odometer_reading) + " miles on it.")

    # 주행거리 속성값을 바꾸는 메서드 추가
    def update_odometer(self, mileage):
        """
        주행거리 표시기를 주어진 값으로 바꿉니다.
        주행거리 표시기를 더 작은 값으로 바꾸려 하면 거부합니다.
        """
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage  # 매개변수로 받은 값을 주행거리 속성에 저장
        else:
            print("주행거리 표시기를 롤백할 수 없습니다.")


my_new_car = Car('audi', 'a4', 2016)
my_new_car.update_odometer(23)  # 매개변수로 주행거리를 넘김
my_new_car.read_odometer()
# This car has 23 miles on it.


print("\n")


# 메서드를 통해 속성값을 정해진 만큼씩만 바꾸기
class Car():
    """자동차를 나타내는 코드"""

    def __init__(self, make, model, year):
        """자동차를 나타내는 속성 초기화"""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0  # 기본값 0

    def get_descriptive_name(self):
        """알아보기 쉬운 이름 변환"""
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()

    def read_odometer(self):
        """주행거리를 나타내는 문장을 출력합니다."""
        print("This car has " + str(self.odometer_reading) + " miles on it.")

    def update_odometer(self, mileage):
        """
        주행거리 표시기를 주어진 값으로 바꿉니다.
        주행거리 표시기를 더 작은 값으로 바꾸려 하면 거부합니다.
        """
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("주행거리 표시기를 롤백할 수 없습니다.")

    # 주행거리 속성값을 지정한 양만큼 늘리는 메서드 추가
    def increment_odometer(self, miles):
        """주행거리를 주어진 양만큼 늘립니다."""
        self.odometer_reading += miles


my_used_car = Car('subaru', 'outback', 2013)
print(my_used_car.get_descriptive_name())

my_used_car.update_odometer(23500)  # 23500 지정
my_used_car.read_odometer()

my_used_car.increment_odometer(100)  # 100 추가
my_used_car.read_odometer()

# 2013 Subaru Outback
# This car has 23500 miles on it.
# This car has 23600 miles on it.
