import unittest
from translator import englishToFrench
from translator import frenchToEnglish

# tests for englishToFrench function
class TestTranslator(unittest.TestCase):
    def test_engishToFrench(self):
        self.assertEqual(englishToFrench('Hello'), '"Bonjour"')
    def test2_engishToFrench(self):
        self.assertNotEqual(englishToFrench('Hello'), '"None"')
    def test_frenchToEnglish(self):
        self.assertEqual(frenchToEnglish('Bonjour'), '"Hello"')
    def test2_frenchToEnglish(self):
        self.assertNotEqual(frenchToEnglish('Bonjour'), '"None"')
if __name__ == "__main__":
    unittest.main()