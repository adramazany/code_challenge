from collections import Counter

'''
1. Hashing and Frequency Maps (Highest Priority)
This is the most common pattern for "logical" questions.
It involves using a dictionary to store counts or indices to avoid nested loops
(improving complexity from O(n^2) to O(n) ).
Key Problems:
Two Sum: Find two numbers in an array that add up to a target.
Valid Anagram: Check if two strings have the same characters.
First Unique Character: Find the first character in a string that doesn't repeat.
Contains Duplicate: Check if any value appears at least twice in an array.
'''


def Two_Sum(array, target):
    '''
    Find two numbers in an array that add up to a target.
    :return:
    '''
    s = set(array)
    for n1 in array:
        if target-n1 in s:
            return n1, target-n1

def Valid_Anagram(s1,s2):
    '''
    Valid Anagram: Check if two strings have the same characters.
    :return:
    '''
    return len(s1)==len(s2) and Counter(s1)==Counter(s2)

def First_Unique_Character(s):
    '''
    First Unique Character: Find the first character in a string that doesn't repeat.
    :return:
    '''
    counter = Counter(s)
    for c,n in counter.items():
        if n==1:
            return c


def Contains_Duplicate(ar):
    '''
    Contains Duplicate: Check if any value appears at least twice in an array.
    :return:
    '''
    # return len(ar)!=len(set(ar))
    seen = set()
    for x in ar:
        if x in seen:
            return True
        seen.add(x)
    return False