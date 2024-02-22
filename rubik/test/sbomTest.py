'''
Created on Jan 17, 2023

@author: Alviere
'''
import unittest
import app

class SbomTest(unittest.TestCase):


    def test_sbom_100_ShouldReturnAuthorName(self):
        expected = 'Alviere'
        result = app._getAuthor('../../')
        actual = result['author']
        self.assertEqual(actual, expected)

if __name__ == '__main__':
    unittest.main()