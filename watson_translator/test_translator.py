import unittest

from translator import translate_to_fr, translate_to_en

class TestTranslator(unittest.TestCase):
    def test_translate_to_fr(self):
        self.assertEqual(translate_to_fr('Hello'), 'Bonjour')

    def test_translate_to_en(self):
        self.assertEqual(translate_to_en('Bonjour'), 'Hello')

unittest.main()