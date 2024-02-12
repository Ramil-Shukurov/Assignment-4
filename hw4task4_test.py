import unittest
from unittest.mock import patch
import io
import Task_4

class TestPalindrome(unittest.TestCase):

    @patch('builtins.input', side_effect=[121, 427787, 22, 12, 313])
    def test_main_input(self, mock_input):
        expected_outputs = [
            "Decimal: 121\nBinary: 1111001\nPalindrome type is only Decimal.\n",
            "Decimal: 427787\nBinary: 1101000011100001011\nPalindrome type is only Binary.\n",
            "Decimal: 22\nBinary: 10110\nPalindrome type is only Decimal.\n",
            "Decimal: 12\nBinary: 1100\nPalindrome type is neither Decimal nor Binary.\n",
            "Decimal: 313\nBinary: 100111001\nPalindrome type is Decimal and Binary.\n"
        ]
        with patch('sys.stdout', new=io.StringIO()) as fake_stdout:
            Task_4.main()
            output = fake_stdout.getvalue()
            self.assertEqual(output, expected_outputs[mock_input.call_count - 1])

    def test_is_Palindrome(self):
        self.assertTrue(Task_4.is_Palindrome(121))
        self.assertTrue(Task_4.is_Palindrome(22))
        self.assertTrue(Task_4.is_Palindrome(0))
        self.assertFalse(Task_4.is_Palindrome(123))
        self.assertFalse(Task_4.is_Palindrome(34))

    def test_to_Binary(self):
        self.assertEqual(Task_4.to_Binary(121), 1111001)
        self.assertEqual(Task_4.to_Binary(22), 10110)
        self.assertEqual(Task_4.to_Binary(0), 0)
        self.assertEqual(Task_4.to_Binary(123), 1111011)
        self.assertEqual(Task_4.to_Binary(34), 100010)

    def test_Palindrome_type(self):
        self.assertEqual(Task_4.Palindrome_type(121), "Palindrome type is only Decimal.")
        self.assertEqual(Task_4.Palindrome_type(22), "Palindrome type is only Decimal.")
        self.assertEqual(Task_4.Palindrome_type(0), "Palindrome type is Decimal and Binary.")
        self.assertEqual(Task_4.Palindrome_type(123), "Palindrome type is neither Decimal nor Binary.")
        self.assertEqual(Task_4.Palindrome_type(34), "Palindrome type is neither Decimal nor Binary.")

if __name__ == "__main__":
    unittest.main()
