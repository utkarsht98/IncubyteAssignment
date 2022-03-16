import unittest
from simple_calculator import SimpleCalculator

class TestAddition(unittest.TestCase):

    def setUp(self):
        self.calculator = SimpleCalculator()
        pass
  
    # Returns True if the add method returns 0 for an empty string.
    def test_strings_empty(self):
        self.assertEqual(self.calculator.Add(""), 0)
  
    # Returns True if the add method returns number for a stirng wtih one number.
    def test_strings_with_one_number(self):      
        self.assertEqual(self.calculator.Add("1"), 1)
        self.assertEqual(self.calculator.Add("12"), 12)
    
    def test_strings_with_two_numbers(self):
        self.assertEqual(self.calculator.Add("2,3"), 5)

    def test_strings_with_more_than_two_numbers(self):
        self.assertEqual(self.calculator.Add("2,3,4"), 9)
        self.assertEqual(self.calculator.Add("20,11,13"), 44)
  
if __name__ == '__main__':
    unittest.main()