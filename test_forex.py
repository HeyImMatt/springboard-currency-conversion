from unittest import TestCase
from forex import get_rate

class ForexFunctionsTests(TestCase):

    def test_conversion(self):
        rate = get_rate('USD', 'EUR', 1)

        print(rate)

        self.assertIn('€', rate)