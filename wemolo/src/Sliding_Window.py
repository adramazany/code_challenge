from collections import deque

'''
3. Sliding Window
Used for finding a "window" (subarray or substring) that meets a specific condition. This is a very common "Medium" level topic.

Key Problems:
Longest Substring Without Repeating Characters: Find the length of the longest unique character sequence.
Maximum Subarray (Kadane’s Algorithm): Find the contiguous subarray with the largest sum.

The Sliding Window technique is an optimization method used to solve problems involving contiguous sequences (subarrays or substrings) in an efficient way.
Instead of using nested loops to re-examine every possible subrange (which takes time), you maintain a "window" of elements and "slide" it across the data.
By updating only the elements that enter or leave the window at each step, you can often reduce the time complexity to

1. Core Logic: How It Works
Think of a bus window or a magnifying glass moving across a line of text.
The State: You keep a running tally (like a sum or a character count) of what is currently inside the window.
The Slide: As the window moves one step to the right:
Add the new element entering from the right.
Remove the old element exiting from the left.
Update your result based on the new window state.

2. Types of Sliding Windows
Fixed-Size Window
The window stays a constant length (
). This is used when the problem asks for something within a subrange of a specific size.
Example: Find the maximum sum of any 3 consecutive numbers in a list.
Action: Move the window one element at a time; subtract the element that just left and add the one that just joined.
Variable-Size (Dynamic) Window
The window grows or shrinks based on a condition.
Example: Find the shortest subarray whose sum is greater than 100.
Action:
Expand the right side until the condition is met.
Shrink from the left to find the smallest valid version of that window.

3. Comparison with Two Pointers
While they both use two markers (left and right), they focus on different things:
Sliding Window: Focuses on the range of elements between the pointers. Every element in the window matters (e.g., calculating their sum).
Two Pointers: Often focuses on the values at the pointers themselves. For example, in a sorted array, you might compare arr[left] and arr[right] to see if they sum to a target.

4. Common Use Cases
You should think of Sliding Window when you see terms like "contiguous subarray," "substring," "maximum/minimum sum," or "longest/shortest sequence" that meets a rule.
Problem Category 	Example (LeetCode)
Unique Elements	Longest Substring Without Repeating Characters
Subarray Sum	Minimum Size Subarray Sum
Frequency	Fruit Into Baskets
Fixed Length	Maximum Average Subarray I

'''

def Longest_Substring_Without_Repeating_Characters(st):
    '''Find the length of the longest unique character sequence.'''
    left = long_l = 0
    right = long_r = 1
    char_map = {}
    char_map[st[left]]=0
    while right < len(st):
        if st[right] in char_map.keys():
            for c in char_map.keys():
                if c == st[right]:
                    left = char_map[c]+1
                    char_map.pop(c)
                    break
                else: char_map.pop(c)
            char_map[st[right]] = right
        else:
            char_map[st[right]] = right
            if (long_r-long_l) < (right-left):
                long_r = right
                long_l = left
    return st[long_l:long_r],long_l,long_r

def length_of_longest_substring(s):
    char_map = {} # {character: last_seen_index}
    left = max_len = 0

    for right, char in enumerate(s):
        if char in char_map and char_map[char] >= left:
            left = char_map[char] + 1
        char_map[char] = right
        max_len = max(max_len, right - left + 1)

    return max_len

def Maximum_Subarray_Kadanes_Algorithm(ar):
    '''Find the contiguous subarray with the largest sum.'''



def max_subarray(nums):
    cur_sum = max_sum = nums[0]
    for num in nums[1:]:
        # Either start a new subarray at current 'num' or keep adding
        cur_sum = max(num, cur_sum + num)
        max_sum = max(max_sum, cur_sum)
    return max_sum
