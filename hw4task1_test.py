import unittest
from unittest.mock import patch
from io import StringIO
import Task_1

class TestCollatzSequence(unittest.TestCase):

    @patch('builtins.input', side_effect=['51'])
    @patch('sys.stdout', new_callable=StringIO)
    def test_collatz_sequence_output(self, mock_stdout, mock_input):
        Task_1.main()
        expected_output = "51 154 77 232 116 58 29 88 44 22 11 34 17 52 26 13 40 20 10 5 16 8 4 2 1\nMax number: 232\n"
        self.assertEqual(mock_stdout.getvalue(), expected_output)

    def test_collatz_sequence_max_collatz_multiple(self):
        test_cases = [(10, 16), (7, 52), (20, 20), (1, 1), (28, 52), (19,88), (51, 232), (192, 192), (12, 16),  (64,64), (3, 16), (58, 88), (8,8), (137, 9232), (47, 9232), (61, 184), (155, 9232,), (60, 160)]
        for input_number, expected_max in test_cases:
            with self.subTest(input_number=input_number, expected_max=expected_max):
                self.assertEqual(Task_1.max_collatz(input_number), expected_max)

if __name__ == "__main__":
    unittest.main()
