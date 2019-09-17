"""Test Spaceman."""
import unittest
from spaceman import is_word_guessed, is_guess_in_word, color


class spacemanTests(unittest.TestCase):
    """Test cases."""

    def test_word_guessed(self):
        """Correctly test whether or not the word is fully guessed."""
        self.assertTrue(is_word_guessed('mouse', ['m', 'o', 'u', 's', 'e']))
        self.assertTrue(is_word_guessed('mouse', ['m', 'b', 'o', 'u', 'z', 's',
                        'e', 'D']))
        self.assertFalse(is_word_guessed('mouse', ['m', 'o', 'u', 's', 'f']))
        self.assertFalse(is_word_guessed('mouse', ['m', '*', 'u', 4, 'f']))

    def test_guess_in_word(self):
        """Correctly check whether guess is in secret word."""
        self.assertTrue(is_guess_in_word("a", "hat"))
        self.assertFalse(is_guess_in_word("A", "hat"))
        self.assertFalse(is_guess_in_word("&", "hat"))

    def test_color(self):
        """Correctly color items."""
        self.assertEqual(color("blue", "blue"), '\033[34mblue\033[00m')


if __name__ == '__main__':
    unittest.main()
