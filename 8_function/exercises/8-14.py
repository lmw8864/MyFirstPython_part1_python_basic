# 8-14.py

"""
8-14. 자동차
"""


def make_car(maker, model_name, **car_info):
    """자동차 정보를 딕셔너리에 저장합니다."""
    car = {}
    car['maker'] = maker
    car['model_name'] = model_name
    for key, value in car_info.items():
        car[key] = value
    return car

car = make_car('벤츠', '2017 벤츠 E클래스 쿠페', color='red', tow_package=True)
print(car)
# {'maker': '벤츠', 'model_name': '2017 벤츠 E클래스 쿠페', 'color': 'red', 'tow_package': True}


def print_car(car):
    """딕셔너리를 매개변수로 받아서 자동차 정보를 출력합니다."""
    print("\n자동차 정보:")
    for key, value in car.items():
        print("\t- " + key.title() + ": " + str(value).title())

print_car(car)
# 자동차 정보:
# 	- Maker: 벤츠
# 	- Model_Name: 2017 벤츠 E클래스 쿠페
# 	- Color: Red
# 	- Tow_Package: True
