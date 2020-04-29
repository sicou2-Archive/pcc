import unittest
from city_functions import a_city

class TestCityFunctions(unittest.TestCase):
    """Tests the city_functions module."""

    def test_city_country(self):
        """Do city/country names like 'Quebec, Canada' work."""
        city_name = a_city('quebec', 'canada')
        self.assertEqual(city_name, 'Quebec, Canada')

    def test_city_country_population(self):
        """Do city/country and populations 'Quebec, Canada, 8_485_000' work?"""
        city_name = a_city('quebec', 'canada', 8_485_000)
if __name__ == '__main__':
    unittest.main()