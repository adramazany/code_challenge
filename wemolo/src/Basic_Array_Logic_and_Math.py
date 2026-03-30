
'''
4. Basic Array Logic & Math
These test your ability to handle indices and basic math without complex algorithms.
Key Problems:
Plus One: Represent a large integer as an array and add one.
Move Zeroes: Move all zeros to the end of an array while maintaining the order of other elements.
Missing Number: Find the one number missing from an array of 0 to n.
'''















def move_zeroes(nums):
    pos = 0 # Pointer for the next non-zero element
    for i in range(len(nums)):
        if nums[i] != 0:
            # Swap current element with the 'pos' pointer
            nums[pos], nums[i] = nums[i], nums[pos]
            pos += 1
    return nums


def plus_one(digits):
    for i in range(len(digits) - 1, -1, -1):
        if digits[i] < 9:
            digits[i] += 1
            return digits
        digits[i] = 0 # Handle carry
    return [1] + digits # If all were 9s (e.g., 999 -> 1000)

def missing_number(nums):
    n = len(nums)
    # Arithmetic series sum formula: n*(n+1)//2
    expected_sum = n * (n + 1) // 2
    return expected_sum - sum(nums)
