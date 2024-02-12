import unittest
from unittest.mock import patch
from io import StringIO
import Task_5
from random import randint

class TestMainFunction(unittest.TestCase):

    def test_main_input(self):
        inputs = [
            (123, 2),  # N = 123, M = 2
            (456, 3),  # N = 456, M = 3
            (89, 1)   # N = 789, M = 4
        ]
        expected_outputs = [
            None,
            None,
            1
        ]
        for i, (N, M) in enumerate(inputs):
            with patch('builtins.input', side_effect=[N, M]):
                with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
                    Task_5.main()
                    output = mock_stdout.getvalue().strip()
                    self.assertEqual(output.split(": ")[1][1:], str(expected_outputs[i]))


    def test_length_num(self):
        num = str(randint(1, 1000000000))
        self.assertEqual(Task_5.length_num(int(num)), len(num))
        self.assertEqual(Task_5.length_num(-123), 0)

    def test_np_to_k(self):
        self.assertEqual(Task_5.np_to_k(695, 2), 2)
        self.assertEqual(Task_5.np_to_k(456, 3), None)
        self.assertEqual(Task_5.np_to_k(89, 1), 1)
        self.assertIsNone(Task_5.np_to_k(0, 0), None)

if __name__ == "__main__":
    unittest.main()
