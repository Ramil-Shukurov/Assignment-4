import unittest
from unittest.mock import patch
from io import StringIO
import Task_2
from random import randint
class TestPolydivisibleNumbers(unittest.TestCase):
    def test_main_input(self):
        test_cases = [
                {'input': '123456', 'expected_output': '1 % 1 = 0\n12 % 2 = 0\n123 % 3 = 0\n1234 % 4 = 2\nFalse\n'},
                {'input': '789', 'expected_output': '7 % 1 = 0\n78 % 2 = 0\n789 % 3 = 0\nTrue\n'},
                {'input': '10203040506070809', 'expected_output': '1 % 1 = 0\n10 % 2 = 0\n102 % 3 = 0\n1020 % 4 = 0\n10203 % 5 = 3\nFalse\n'},
                {'input': '122', 'expected_output': '1 % 1 = 0\n12 % 2 = 0\n122 % 3 = 0\nTrue\n'},
                {'input': '0', 'expected_output': 'True\n'}
        ]
        for test_case in test_cases:
            with patch('builtins.input', return_value=test_case['input']), patch('sys.stdout', new_callable=StringIO) as mock_stdout:
                Task_2.main()
                self.assertEqual(mock_stdout.getvalue(), test_case['expected_output'])

    def test_length_num(self):
        num = str(randint(1, 1000000000))
        self.assertEqual(Task_2.length_num(12345), 5)
        self.assertEqual(Task_2.length_num(657412038), 9)
        self.assertEqual(Task_2.length_num(9), 1)
        self.assertEqual(Task_2.length_num(int(num)), len(num))

    def test_is_polydivisible(self):
        self.assertTrue(Task_2.is_polydivisible(1624, 4))
        self.assertFalse(Task_2.is_polydivisible(122, 3))
        self.assertTrue(Task_2.is_polydivisible(162, 3))
        self.assertFalse(Task_2.is_polydivisible(123456789, 9))

if __name__ == "__main__":
    unittest.main()
