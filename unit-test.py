import unittest
from main import factors 
from main import is_prime 
from main import vowels 

class TestMain(unittest.TestCase):

    def test_vowels(self):
        self.assertEqual(vowels("love"), ['o','e'])
        self.assertEqual(vowels("hate"), ['a','e'])

    def test_factors(self):
        self.assertEqual(factors(1), [1])
        self.assertEqual(factors(2), [2])

    def test_is_prime(self):
        self.assertTrue(is_prime(3))
        self.assertFalse(is_prime(4))

    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')
    
if __name__ == '__main__':
    unittest.main()