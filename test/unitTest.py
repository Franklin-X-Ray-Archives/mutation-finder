import unittest

class utest_mutation_finder(unittest.TestCase):
    """docstring for utest_mutation_finder."""
    def __init__(self, arg):
        super(utest_mutation_finder, self).__init__()
        self.arg = arg

    def setUp(self):
        print("SetUp")

if __name__ == '__main__':
    unittest.main()
