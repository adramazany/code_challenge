

'''
5. Essential Pythonic Tricks
For these interviews, knowing how to manipulate strings and lists quickly in Python is a huge advantage:
Slicing: s[::-1] to reverse a string or s[1:5] for substrings.
List Comprehensions: Fast ways to filter or transform data.
Sorting: sorted(string) returns a list of characters in order, which is great for anagram checks.
String to List: Use list(string) because Python strings are immutable; you must convert them to a list to change characters in-place.



5. Pythonic Tricks (The "One-Liners")
Interviewers love to see that you actually know Python's built-in power.
Check Anagram: sorted(s1) == sorted(s2)
Reverse Words: " ".join(s.split()[::-1])
Remove Duplicates (order doesn't matter): list(set(nums))
Fast Counts: from collections import Counter; counts = Counter(nums)


'''





