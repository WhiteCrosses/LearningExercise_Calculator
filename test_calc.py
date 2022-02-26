import unittest
import Calculator_Excercise as cp


class TestCalculator(unittest.TestCase):

    def test_calc(self):
        result = cp.calc(0, '2+2')
        self.assertEqual(result, 4)

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
