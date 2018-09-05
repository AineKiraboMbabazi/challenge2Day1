from dictionary import dictionary
import unittest


class Testtest(unittest.TestCase):

    def test_dictionary(self):
        self.assertEqual(dictionary(2,15), {2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81, 10: 100, 11: 121, 12: 144, 13: 169, 14: 196})
        self.assertEqual(dictionary(7,8), {7: 49})
        
          




if __name__ == '__main__':
    unittest.main()