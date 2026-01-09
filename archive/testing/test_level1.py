import unittest
from calculator import Calculator

class TestOperations(unittest.TestCase):
    
    def setUp(self):
        self.calc = Calculator(8, 2)

    def test_sum(self):
        answer = self.calc.get_sum()
        print(f"Sum Test Answer: {answer}. \n Test Results:")
        self.assertEqual(self.calc.get_sum(), 10,"Answer was not 10")

    def test_subtraction(self):
        answer = self.calc.get_differrence()
        print(f"Sub Test Answer: {answer}. \n Test Results:")
        self.assertEqual(self.calc.get_differrence(), 6,"Answer was not 6")

    def test_multiplication(self):   
        answer = self.calc.get_product()
        print(f"Mult Test Answer: {answer}. \n Test Results:")
        self.assertEqual(self.calc.get_product(), 16,"Answer was not 16")
    
    def test_division(self):
        answer = self.calc.get_quotient()
        print(f"Div Test Answer: {answer}. \n Test Results:")
        self.assertEqual(self.calc.get_quotient(), 4,"Answer was not 4")

if __name__ == '__main__':
    unittest.main()