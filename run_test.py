import unittest

import run


class TestRun(unittest.TestCase):

    def test_execute(self):
        self.assertEqual(2, run.execute(1))

    def test_myexecution(self):
        self.assertEqual(20, run.myexecution(4))


if __name__ == '__main__':
    unittest.main()
