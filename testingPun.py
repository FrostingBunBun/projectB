import unittest
from pun import Pun

class TestPun(unittest.TestCase):
    def setUp(self):
        self.pun = Pun()

    def test_evaluation(self):
        with open('test.txt', 'r') as f:
            lines = f.readlines()
            for line in lines:

                line = line.strip()
                with self.subTest(line=line):
                    self.pun.run(line)

if __name__ == '__main__':
    unittest.main()
