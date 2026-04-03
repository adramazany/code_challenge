from unittest import TestCase
from src.Array_String import Solution


class TestSolution(TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_max_profit(self):
        self.fail()

    def test_can_jump(self):
        self.assertTrue(self.solution.canJump([2, 3, 1, 1, 4]))
        self.assertFalse(self.solution.canJump([3, 2, 1, 0, 4]))

    def test_h_index(self):
        self.assertEqual(self.solution.hIndex([3, 0, 6, 1, 5]), 3)
        self.assertEqual(self.solution.hIndex([1, 3, 1]), 1)
        self.assertEqual(self.solution.hIndex([100]), 1)
        self.assertEqual(self.solution.hIndex([0]), 0)

    def test_product_except_self(self):
        self.assertListEqual(self.solution.productExceptSelf([1, 2, 3, 4]), [24, 12, 8, 6])
        self.assertListEqual(self.solution.productExceptSelf([-1, 1, 0, -3, 3]), [0, 0, 9, 0, 0])

    def test_candy(self):
        self.assertEqual(self.solution.candy([1,0,2]), 5)
        self.assertEqual(self.solution.candy([1,2,2]), 4)
