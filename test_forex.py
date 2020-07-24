from unittest import TestCase
from forex import get_rate, validate_code

class ForexFunctionsTests(TestCase):

    def test_code_validation(self):
        valid_code = validate_code('USD')
        invalid_code = validate_code('ZZZ')

        self.assertTrue(valid_code)
        self.assertFalse(invalid_code)

    def test_conversion(self):
        rate = get_rate('USD', 'EUR', 1)

        self.assertIn('€', rate)