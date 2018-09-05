from computeAge import computeAge
import unittest


class Testtest(unittest.TestCase):

    def test_computeAge(self):
        self.assertEqual(computeAge(2015), 'you are a minor')
        self.assertEqual(computeAge(2000), 'you are a youth')
        self.assertEqual(computeAge(1970), 'you are an elder')
        self.assertEqual(computeAge(2019), 'you can not have a negative age')
    @unittest.skip('work in progress')
    def test_input_is_int(self):
        self.assertRaises(computeAge('yob'),ValueError )   




if __name__ == '__main__':
    unittest.main()
    