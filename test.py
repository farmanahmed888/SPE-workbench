import unittest
from Prog1 import summation
class Testsum (unittest.TestCase):
    def test_summation(self):
        self.assertEqual(summation([1, 2, 3]), 6)
        self.assertEqual(summation([1, 2, 3, 4]), 10)
        self.assertEqual(summation([1, 2, 3, 4, 5]), 15)
if __name__ == '__main__':
    unittest.main()