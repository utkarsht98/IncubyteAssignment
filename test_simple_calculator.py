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
    
    # Returns True if the add method returns sum for a string wtih one number and multiple digits.
    def test_with_one_number_multiple_digits(self):
        self.assertEqual(self.calculator.Add("12"), 12)
    
    # Returns True if the method returns sum for two numbers.
    def test_with_two_numbers(self):
        self.assertEqual(self.calculator.Add("2,3"), 5)

    # Returns True if the method returns sum for multiple numbers.
    def test_with_multiple_numbers(self):
        self.assertEqual(self.calculator.Add("20,11,13"), 44)
    
    # Returns sum for multiple numbers after removing delimiters.
    def test_new_line_delimiter_1(self):
        self.assertEqual(self.calculator.Add('1\n2,3'), 6)

    # Returns sum for multiple numbers after removing delimiters.
    def test_new_line_delimiter_2(self):
        self.assertEqual(self.calculator.Add("4\n1\n3,2,10,8\n6"), 34)
    
    # Returns sum after removing changed delimiter.
    def test_changing_delimiter_addition(self):
        self.assertEqual(self.calculator.Add("//;\n1;28;3;12;8;6"), 58)
    
    # Returns an error message for negative values.
    def test_negative_values_error(self):
        self.assertEqual(self.calculator.Add("-12,20\n3,-4\n-2,-8"), "Negatives not allowed --->-12,-4,-2,-8")
    
    # Returns an error message for negative values after removal of changed delimiters.
    def test_negative_values_error_with_delimiter_change(self):
        self.assertEqual(self.calculator.Add("//;\n-12;20;3;-4;-2;-8"), "Negatives not allowed --->-12,-4,-2,-8")
  
if __name__ == '__main__':
    unittest.main()