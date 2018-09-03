from dictionary import dictionary
import unittest


class Testtest(unittest.TestCase):

    def test_dictionary(self):
        self.assertEqual(dictionary(2,3), {2: 4})
        self.assertEqual(dictionary(7,8), {7: 49})
        
          




if __name__ == '__main__':
    unittest.main()