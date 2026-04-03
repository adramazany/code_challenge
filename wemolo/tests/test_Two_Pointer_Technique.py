from unittest import TestCase

from sortedcontainers import SortedList

from src.Two_Pointer_Technique import Valid_Palindrome, Remove_Duplicates_from_Sorted_Array, Merge_Sorted_Arrays, \
    Reverse_String, removeDuplicatesII, rotate


class Test(TestCase):
    def test_valid_palindrome(self):
        self.assertTrue(Valid_Palindrome("A man. a plan, a canal: Panama"))
        self.assertFalse(Valid_Palindrome("ABCba1"))
        self.assertTrue(Valid_Palindrome("ABC1cba"))

    def test_reverse_string(self):
        ar = list("Ab1Cd")
        Reverse_String(ar)
        self.assertEqual(ar, list("dC1bA"))

    def test_remove_duplicates_from_sorted_array(self):
        ar = SortedList([1, 1, 3, 1, 2, 2, 4, 4, 4, 4, 5, 5, 6, 7, 8, 8, 8, 9, 10, 10])
        Remove_Duplicates_from_Sorted_Array(ar)
        self.assertEqual(ar, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

    def test_merge_sorted_arrays(self):
        sar = Merge_Sorted_Arrays([1, 1, 2, 2, 4, 4], [0, 1, 2, 3, 4, 5])
        print(">>>>>>>>>", sar)
        self.assertEqual(sar, [0, 1, 1, 1, 2, 2, 2, 3, 4, 4, 4, 5])

    def test_remove_duplicates_ii(self):
        ar = [1, 1, 1, 2, 2, 3]
        k = removeDuplicatesII(ar)
        self.assertListEqual(ar[:k], [1, 1, 2, 2, 3])

    def test_rotate(self):
        ar = [1,2,3,4,5,6]
        rotate(ar,3)
        self.assertListEqual(ar, [4,5,6,1,2,3])
        ar = [1,2,3,4,5,6,7]
        rotate(ar,3)
        self.assertListEqual(ar, [5,6,7,1,2,3,4])
