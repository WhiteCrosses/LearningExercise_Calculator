import unittest
import Calculator_Excercise as cp


class TestCalculator(unittest.TestCase):

    def test_calc(self):
        result = cp.calc(0, '3+2')
        self.assertEqual(result, 5)

        result = cp.calc(0, '3/0')
        self.assertEqual(result, 'invalid_operation')

        result = cp.calc(3, '+2*4')
        self.assertEqual(result, 11)

    def test_filter(self):
        result = cp.filter(0, '7h83f4+923-9f3')
        self.assertEqual(result, '7834+923-93')

    def test_response(self):
        result = cp.response(0, 'quit')
        self.assertNotEqual(result, True)

    def test_myeval1(self):
        result = cp.myeval1('2+3')
        self.assertIsInstance(result, int)

    def test_myeval2(self):
        result = cp.myeval2('3', '2+3')
        self.assertNotIsInstance(result, str)


if __name__ == '__main__':
    unittest.main()
