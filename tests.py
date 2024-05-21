from main import get_unique_and_broken_lines
import unittest


class TestsMainMethods(unittest.TestCase):
    def test_get_unique_and_broken_lines(self):
        [data, broken] = get_unique_and_broken_lines("data/n_1.csv")
        self.assertEqual(broken[0]['id'], "457865234-3431")
        self.assertEqual(len(data), 4)
        self.assertEqual(len(broken), 5)
