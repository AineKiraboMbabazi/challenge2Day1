import unittest
from computeage.computeage import compute_age


class TestComputeAge(unittest.TestCase):

    def test_computeAge(self):
        self.assertEqual(compute_age(2015), 'you are a minor')
        self.assertEqual(compute_age(2000), 'you are a youth')
        self.assertEqual(compute_age(1970), 'you are an elder')
        self.assertEqual(compute_age(2019), 'you can not have a negative age')
    
    def test_input_is_int(self):
        self.assertRaises(ValueError ,compute_age,'yob')   




if __name__ == '__main__':
    unittest.main()
    