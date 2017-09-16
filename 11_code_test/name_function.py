# name_function.py


# def get_formatted_name(first, middle, last):  # 중간 이름 매개변수 추가
#     """읽기 좋은 전체 이름을 생성합니다."""
#     full_name = first + ' ' + middle + ' ' + last
#     return full_name.title()


# 중간 이름을 옵션으로 만들고, 중간 이름 여부에 따라 동작을 달리하는 if문 추가

def get_formatted_name(first, last, middle=''):  # 중간 이름을 마지막에 위치, 빈 기본값 설정
    """읽기 좋은 전체 이름을 생성합니다."""
    if middle:
        full_name = first + ' ' + middle + ' ' + last
    else:
        full_name = first + ' ' + last
    return full_name.title()
