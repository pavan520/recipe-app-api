from django.test import TestCase
from app.app import calc


class CalcTest(TestCase):
    def test_add_number(self):
        """ Tests that two numbers are added together """
        self.assertEqual(calc.add(3, 8), 11)

    def test_subtract_numbers(self):
        """ Tests that two numbers are subtracted """
        self.assertEqual(calc.subtract(5, 11), 6)
