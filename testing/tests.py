import unittest
from xmass_trees import (tree_1,
                         tree_2,
                         tree_3,
                         TreeObj)
from xmass_postcard import Postcard
from testing.correct_trees import (CORRECT_TREE_1,
                                   CORRECT_TREE_2,
                                   CORRECT_TREE_3_1,
                                   CORRECT_TREE_3_2,
                                   CORRECT_POSTCARD)


class TestTree1(unittest.TestCase):

    def test_tree_1(self):
        t1 = tree_1(5)

        self.assertEqual(t1, CORRECT_TREE_1)

    def test_tree_2(self):
        t2 = tree_2(5)

        self.assertEqual(t2, CORRECT_TREE_2)

    def test_tree_3_1(self):
        t3 = tree_3(5, 1)

        self.assertEqual(t3, CORRECT_TREE_3_1)

    def test_tree_3_2(self):
        t3 = tree_3(5, 3)

        self.assertEqual(t3, CORRECT_TREE_3_2)

    def test_postcard(self):
        postcard = Postcard()
        postcard.place("Merry Xmas", 27, 19)

        test_input = "7 3 7 37 4 2 10 25 11 1 5 14 10 4 9 30 5 4 16 19"
        test_input = [int(x) for x in test_input.split()]

        trees_data = [test_input[i:i + 4] for i in range(0, len(test_input), 4)]

        trees = []
        for index, [lines, interval, y, x] in enumerate(trees_data, start=1):
            trees.append(TreeObj(index, lines, interval, y, x))

        for tree in trees:
            postcard.place(tree)

        self.assertEqual(str(postcard), CORRECT_POSTCARD)


if __name__ == "__main__":
    unittest.main()
