import unittest
from roman_numerals import roman


class TestRoman(unittest.TestCase):
    def test_roman(self):
        self.assertEqual(roman("MCMXCVII"), 1997)
        self.assertEqual(roman("XL"), 40)
        self.assertEqual(roman("MCMXCIV"), 1994)
        self.assertEqual(roman("MDCCLXXVI"), 1776)
        self.assertEqual(roman("MMXIV"), 2014)
        self.assertEqual(roman("mmxiv"), 2014)
        self.assertEqual(roman("xl"), 40)

        """Tests for invalid numerals"""
        with self.assertRaises(ValueError):
            roman("XS")


if __name__ == '__main__':
    unittest.main()
