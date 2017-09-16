# 11-1_2_test_cities.py

"""
11-1. 도시와 국가
11-2. 인구
"""
import unittest
from city_function import city


class TestCity(unittest.TestCase):
    """city_function.py 테스트"""

    def test_city_country(self):
        """'santiago', 'chile' 같은 값으로 호출했을 때 정확한 문자열이 반환되는가?"""
        city_country = city('santiago', 'chile')
        self.assertEqual(city_country, "City: Santiago\nCountry: Chile")

    def test_city_country_population(self):
        """'santiago', 'chile', 5000000 같은 값으로 호출했을 때 정확한 문자열이 반환되는가?"""
        city_country = city('santiago', 'chile', 5000000)
        self.assertEqual(city_country, "City: Santiago\nCountry: Chile\nPopulation: 5000000")

if __name__ == "__main__":
    unittest.main()
