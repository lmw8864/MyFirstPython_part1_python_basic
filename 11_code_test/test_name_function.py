# test_name_function.py

import unittest
from name_function import get_formatted_name


# 테스트 케이스 클래스
class NamesTestCase(unittest.TestCase):  # 반드시 unittest.TestCase 를 상속
    """name_function.py 테스트"""

    # 단위 테스트 메서드
    def test_first_last_name(self):  # 반드시 test_ 로 시작
        """'Janis Joplin' 같은 이름이 동작하는지?"""
        formatted_name = get_formatted_name('janis', 'joplin')
        self.assertEqual(formatted_name, 'Janis Joplin')  # 첫 번째 인자와 두 번째 인자가 일치하는지 비교

    # 단위 테스트 메서드 추가
    def test_first_last_middle_name(self):
        """'Wolfgang Amadeus Mozart' 같은 이름이 동작하는지?"""
        formatted_name = get_formatted_name('wolfgang', 'mozart', 'amadeus')
        self.assertEqual(formatted_name, 'Wolfgang Amadeus Mozart')

# unittest.main()  # 이 파일에 들어있는 테스트를 실행

if __name__ == "__main__":
    unittest.main()

# ※ 'test_' 로 시작하는 메서드는 test_name_function.py 를 실행할 때 자동으로 실행됩니다.
# ※ 파이참에서 실행하는 것보다 터미널에서 실행하는 것이 더 정확하게 나온다.
