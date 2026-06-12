import unittest
from app import is_leap_year

class TestLeapYear(unittest.TestCase):

    def test_year_2026_is_leap_year(self):
        self.assertFalse(is_leap_year(2026))
    
    def test_year_2000_is_leap_year(self):
        self.assertTrue(is_leap_year(2000))

    def test_year_146_is_not_leap_year(self):
        self.assertFalse(is_leap_year(146))

    def test_year_2024_is_leap_year(self):
        self.assertTrue(is_leap_year(2024))

    def test_year_2023_is_not_leap_year(self):
        self.assertFalse(is_leap_year(2023))

if __name__ == "__main__":
    unittest.main()
