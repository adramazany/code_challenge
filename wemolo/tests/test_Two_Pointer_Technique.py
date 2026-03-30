from unittest import TestCase
from src.Two_Pointer_Technique import Valid_Palindrome,Remove_Duplicates_from_Sorted_Array, Merge_Sorted_Arrays, Reverse_String

class Test(TestCase):
    def test_valid_palindrome(self):
        self.assertTrue( Valid_Palindrome("A man. a plan, a canal: Panama") )
        self.assertFalse( Valid_Palindrome("ABCba1") )
