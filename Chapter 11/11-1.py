import unittest
from city_functions import city_country

class TestCityCountry(unittest.TestCase):
    """Tests for the city_country() function."""

    def test_city_country(self):
        """Verifies correct formatting of 'City, Country'."""
        formatted_string = city_country('Santiago', 'Chile')
        self.assertEqual(formatted_string, 'Santiago, Chile')

        # Additional test cases
        self.assertEqual(city_country('Paris', 'France'), 'Paris, France')
        self.assertEqual(city_country('Tokyo', 'Japan'), 'Tokyo, Japan')

if __name__ == '__main__':
    unittest.main()
