import unittest

from arithmetic import arithmetic_arranger

class TestArithmeticArranger(unittest.TestCase):

    def test_valid_problems(self):
        problems = ["32 + 698", "3801 - 2", "45 + 43", "123 + 49"]
        result = arithmetic_arranger(problems)
        expected = "   32      3801      45      123\n+ 698    -    2    + 43    +  49\n-----    ------    ----    -----"
        self.assertEqual(result, expected)
        
        problems = ["32 + 8", "1 - 3801", "9999 + 9999", "523 - 49"]
        result = arithmetic_arranger(problems)
        expected = "   32         1      9999      523\n+  8    - 3801    + 9999    -  49\n----    ------    ------    -----"
        self.assertEqual(result, expected)
        
    def test_too_many_problems(self):
        problems = ["32 + 8", "1 - 3801", "9999 + 9999", "523 - 49", "1 + 2", "3 + 4"]
        result = arithmetic_arranger(problems)
        self.assertEqual(result, "Error: Too many problems.")
        
    def test_invalid_operator(self):
        problems = ["32 * 8", "1 - 3801"]
        result = arithmetic_arranger(problems)
        self.assertEqual(result, "Error: Operator must be '+' or '-'.")
        
        problems = ["32 / 8", "1 + 1"]
        result = arithmetic_arranger(problems)
        self.assertEqual(result, "Error: Operator must be '+' or '-'.")
        
    def test_non_digit_operands(self):
        problems = ["32 + 8", "one - 3801"]
        result = arithmetic_arranger(problems)
        self.assertEqual(result, "Error: Numbers must only contain digits.")
        
        problems = ["32 + eight", "1 + 1"]
        result = arithmetic_arranger(problems)
        self.assertEqual(result, "Error: Numbers must only contain digits.")
        
    def test_operands_too_long(self):
        problems = ["32 + 8", "12345 - 6789"]
        result = arithmetic_arranger(problems)
        self.assertEqual(result, "Error: Numbers cannot be more than four digits.")
        
        problems = ["1234 + 56789", "1 + 1"]
        result = arithmetic_arranger(problems)
        self.assertEqual(result, "Error: Numbers cannot be more than four digits.")

if __name__ == '__main__':
    unittest.main()