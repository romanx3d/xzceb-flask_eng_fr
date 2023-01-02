import unittest
from translator import english_to_french,french_to_english

class TestTranslation(unittest.TestCase):

    def test_english_to_french(self):
        self.assertEqual(english_to_french('Hello'), 'Bonjour')
        self.assertEqual(english_to_french(''), 'null input')

    def test_french_to_english(self):
        self.assertEqual(french_to_english('Bonjour'), 'Hello')
        self.assertEqual(french_to_english(''), 'null input')

   
if __name__ == '__main__':
    unittest.main()