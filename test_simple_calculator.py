import unittest
from simple_calculator import SimpleCalculator

class TestAddition(unittest.TestCase):

    def setUp(self):
        self.calculator = SimpleCalculator()
    
    def tearDown(self) -> None:
        return super().tearDown()
  
    # Returns True if the add method returns 0 for an empty string.
    def test_strings_empty(self):
        self.assertEqual(self.calculator.Add(""), 0)
  
    # Returns True if the add method returns number for a stirng wtih one number.
    def test_with_one_number_single_dgit(self):      
        self.assertEqual(self.calculator.Add("1"), 1)
    
    def test_with_one_number_multiple_digits(self):
        self.assertEqual(self.calculator.Add("12"), 12)
    
    def test_with_two_numbers(self):
        self.assertEqual(self.calculator.Add("2,3"), 5)

    def test_with_more_than_two_numbers(self):
        self.assertEqual(self.calculator.Add("20,11,13"), 44)
    
    def test_new_line_delimiter_1(self):
        self.assertEqual(self.calculator.Add('1\n2,3'), 6)

    def test_new_line_delimiter_2(self):
        self.assertEqual(self.calculator.Add("4\n1\n3,2,10,8\n6"), 34)
  
if __name__ == '__main__':
    unittest.main()