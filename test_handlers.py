from unittest import TestCase
from handlers import form_validate

class HandlersTests(TestCase):

    def test_input_validation(self):
        self.assertIn('From code not valid', form_validate('ZZZ', 'USD', '1.00'))
        self.assertIn('To code not valid', form_validate('USD', 'ZZZ', '1.00'))
        self.assertIn('Amount needs to be a valid number', form_validate('USD', 'EUR', 'ZZZ'))
        self.assertIs(form_validate('USD', 'EUR', '1'), True)