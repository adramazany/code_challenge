from unittest import TestCase
from src.Hashing_and_Frequency_Maps import Two_Sum, Valid_Anagram, Contains_Duplicate, First_Unique_Character


class Test(TestCase):
    def test_two_sum(self):
        ar = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        target = 15
        n1, n2 = Two_Sum(ar, target)
        print(f">>>>>>>>>>>>>>> {n1}+{n2}={target}")
        self.assertEqual(n1 + n2, target)

    def test_valid_anagram(self):
        self.assertTrue(Valid_Anagram("abcaba", "abacba"))
        self.assertFalse(Valid_Anagram("abcaaba", "abaabc"))

    def test_first_unique_character(self):
        self.assertEqual(First_Unique_Character("abcba"), "c")
        self.assertEqual(First_Unique_Character("abcbac z"), " ")
        self.assertEqual(First_Unique_Character("abcbac"), None)

    def test_contains_duplicate(self):
        self.assertTrue( Contains_Duplicate( ["apple", "orange", "peach", "apple"] ) )
        self.assertFalse( Contains_Duplicate( [1,2, 3, 4, 5, 6, 7, 8, 9] ))
