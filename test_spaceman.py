"""Test Spaceman."""
import unittest
from spaceman import is_word_guessed


class spacemanTests(unittest.TestCase):
    """Test cases."""

    def test_word_guessed(self):
        """Correctly test whether or not the word is fully guessed."""
        self.assertTrue(is_word_guessed('mouse', ['m', 'o', 'u', 's', 'e']))
        self.assertTrue(is_word_guessed('mouse', ['m', 'b', 'o', 'u', 'z', 's',
                        'e', 'D']))
        self.assertFalse(is_word_guessed('mouse', ['m', 'o', 'u', 's', 'f']))
        self.assertFalse(is_word_guessed('mouse', ['m', '*', 'u', 4, 'f']))


if __name__ == '__main__':
    unittest.main()
