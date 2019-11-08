import unittest
import binary_tree as bt


class Test_Add(unittest.TestCase):
    def test_add_basic(self):
        node = bt.Node(50, 3)
        self.assertEqual(node.key, 50)
        self.assertEqual(node.value, 3)

if __name__ == '__main__':
    unittest.main()
