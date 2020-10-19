import unittest
from random import randint

import program


class TestTermFrequencyCalc(unittest.TestCase):
    text = "baz bar foo foo zblah zblah zblah baz toto bar"
    result = [("zblah", 3), ("bar", 2), ("baz", 2)]

    def testSizeFrequency(self):
        random_num = randint(1, 10)
        self.assertEqual(len(program.termFrequency(self.text, random_num)), random_num)

    def testHardCodedFrequency(self):
        self.assertEqual(program.termFrequency(self.text, 3), self.result)


if __name__ == '__main__':
    unittest.main()
