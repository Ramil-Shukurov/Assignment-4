import unittest
from unittest.mock import patch
from io import StringIO
import Task_2
from random import randint
class TestPolydivisibleNumbers(unittest.TestCase):


    @patch('builtins.input', side_effect=['123456', '789', '10203040506070809', '0'])
    @patch('sys.stdout', new_callable=StringIO)
    def test_main_input(self, mock_stdout, mock_input):
        Task_2.main()
        expected_output = "1 % 1 = 0\n2 % 2 = 0\n3 % 3 = 0\n4 % 4 = 0\n5 % 5 = 0\n6 % 6 = 0\nTrue\n"\
                          "7 % 1 = 0\n8 % 2 = 0\n9 % 3 = 0\nFalse\n"\
                          "1 % 1 = 0\n0 % 2 = 0\n2 % 3 = 0\n0 % 4 = 0\n3 % 5 = 0\n0 % 6 = 0\n4 % 7 = 0\n5 % 8 = 0\n6 % 9 = 0\n7 % 10 = 0\n8 % 11 = 0\n9 % 12 = 0\nTrue\n"\
                          "Enter a number (N>0): \nTrue\n"
        self.assertEqual(mock_stdout.getvalue(), expected_output)

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
