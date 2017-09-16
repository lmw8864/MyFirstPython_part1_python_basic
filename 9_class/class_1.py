# class_1.py

"""
Dog 클래스 만들기
"""


# 클래스 이름의 첫 글자는 대문자
class Dog():
    """개를 모델화하는 시도"""

    # 새 인스턴스를 만들 때마다 자동으로 실행되는 __init__() 메서드
    def __init__(self, name, age):
        # self 매개변수는 메서드를 정의할 때 필수이며, 반드시 다른 매개변수보다 먼저 써야 합니다.
        """name과 age 속성 초기화"""
        self.name = name
        self.age = age
        # self.name 과 self.age 는 클래스의 모든 메서드에서 접근할 수 있으며,
        # 이 클래스에서 만든 모든 인스턴스에서 접근할 수 있습니다.(속성)

    # 메서드 정의
    def sit(self):
        """명령에 따라 앉는 개"""
        print(self.name.title() + " is now sitting.")

    def roll_over(self):
        """명령에 따라 구르는 개"""
        print(self.name.title() + " rolled over!")


# my_dog 인스턴스 생성
my_dog = Dog('willie', 6)

# 속성에 접근하기(점 표기법)
print("My dog's name is " + my_dog.name.title() + ".")  # Dog 클래스의 self.name 속성
print("My dog's " + str(my_dog.age) + " years old.")
# My dog's name is Willie.
# My dog's 6 years old.

# 메서드 호출하기(점 표기법)
my_dog.sit()
my_dog.roll_over()
# Willie is now sitting.
# Willie rolled over!

# your_dog 인스턴스 생성
your_dog = Dog('lucy', 3)

# my_dog 와 your_dog 는 고유의 속성을 갖고 같은 동작을 할 수 있는 별도의 인스턴스
