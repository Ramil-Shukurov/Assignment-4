import unittest
from unittest.mock import patch
from io import StringIO
import Task_3
from random import randint


class TestLookAndSay(unittest.TestCase):

    @patch('builtins.input', side_effect=[112233, 101010, 123, 5, 0])
    def test_main_input(self, mock_input):
        expected_outputs = ["122333\n", "000\n", "invalid\n", "invalid\n", "\n"]
        with patch('sys.stdout', new=StringIO()) as fake_stdout:
            Task_3.main()
            output = fake_stdout.getvalue()
            self.assertEqual(output, expected_outputs[mock_input.call_count - 1])

    def test_look_and_say(self):
        # Test cases for valid inputs
        self.assertEqual(Task_3.look_and_say(112233), "122333")
        self.assertEqual(Task_3.look_and_say(101010), "000")
        self.assertEqual(Task_3.look_and_say(122333), "233333")
        self.assertEqual(Task_3.look_and_say(111222), "1222")
        self.assertEqual(Task_3.look_and_say(111223), "1233")

    def test_invalid_look_and_say(self):
        # Test case for invalid input (odd length number)
        self.assertEqual(Task_3.look_and_say(14923), "invalid")

        # Test case for single-digit number
        self.assertEqual(Task_3.look_and_say(5), "invalid")

        # Test case for zero
        self.assertEqual(Task_3.look_and_say(0), "")
    
    def test_length_num(self):
        num = str(randint(1, 1000000000))
        self.assertEqual(Task_3.length_num(int(num)), len(num))

if __name__ == "__main__":
    unittest.main()
