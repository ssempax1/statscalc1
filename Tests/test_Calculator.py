import unittest
from Calculator.Calculator import Calculator
from CSVReader.CsvReader import CsvReader


class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.calculator = Calculator()

    def test_instantiate_calculator(self):
        self.assertIsInstance(self.calculator, Calculator)

    def test_addition(self):
        test_data = CsvReader("Tests/Data/Unit_Test_Calculator.csv").data
        for row in test_data:
            result = float(row['Add Result'])
            self.assertEqual(self.calculator.add(row['Add 1'], row['Add 2']), float(row['Add Result']))
            self.assertEqual(self.calculator.result, result)

    def test_subtraction(self):
        test_data = CsvReader("Tests/Data/Unit_Test_Calculator.csv").data
        for row in test_data:
            result = float(row['Sub Result'])
            self.assertEqual(self.calculator.subtract(row['Sub 1'], row['Sub 2']), float(row['Sub Result']))
            self.assertEqual(self.calculator.result, result)

    def test_multiplication(self):
        test_data = CsvReader("Tests/Data/Unit_Test_Calculator.csv").data
        for row in test_data:
            result = float(row['Multiply Result'])
            self.assertEqual(self.calculator.multiply(row['Multiply 1'], row['Multiply 2']), float(row['Multiply Result']))
            self.assertEqual(self.calculator.result, result)

    def test_division(self):
        test_data = CsvReader("Tests/Data/Unit_Test_Calculator.csv").data
        for row in test_data:
            result = float(row['Divide Result'])
            self.assertEqual(self.calculator.division(row['Divide 1'], row['Divide 2']), float(row['Divide Result']))
            self.assertEqual(self.calculator.result, result)

    def test_squared(self):
        test_data = CsvReader("Tests/Data/Unit_Test_Calculator.csv").data
        for row in test_data:
            result = float(row['Squared Result'])
            self.assertEqual(self.calculator.squared(row['Squared 1']), float(row['Squared Result']))
            self.assertEqual(self.calculator.result, result)

    def test_sqrt(self):
        test_data = CsvReader("Tests/Data/Unit_Test_Calculator.csv").data
        for row in test_data:
            result = float(row['Sqrt Result'])
            self.assertEqual(self.calculator.sqrt(row['Sqrt 1']), float(row['Sqrt Result']))
            self.assertEqual(self.calculator.result, result)

    def test_results_property(self):
        self.assertEqual(self.calculator.result, 0)


if __name__ == '__main__':
    unittest.main()
