import unittest
import translator

class TestEnFr(unittest.TestCase): 
    def test1(self): 
        self.assertNotEqual(translator.english_to_french(), 'Bonjour') 
        self.assertEqual(translator.english_to_french('Hello'), 'Bonjour') 


class TestFrEn(unittest.TestCase): 
    def test1(self): 
        self.assertNotEqual(translator.french_to_english(), 'Hello') 
        self.assertEqual(translator.french_to_english('Bonjour'),'Hello') 

unittest.main()