


'''
2. Two-Pointer Technique
This pattern is essential for linear structures like strings and sorted arrays.
You typically use one pointer at the start and one at the end (or two moving at different speeds)
Key Problems:
Valid Palindrome: Check if a string reads the same forward and backward after cleaning.
Reverse String: Reverse an array of characters in-place.
Remove Duplicates from Sorted Array: Modify an array in-place to remove duplicates.
Merge Sorted Arrays: Combine two sorted arrays into one.

'''
from typing import List


def Valid_Palindrome(st):
    '''Check if a string reads the same forward and backward after cleaning.'''
    #cleaned = "".join( c.lower() for c in st if c.isalnum() )
    #return cleaned == cleaned[::-1]
    i = 0
    r = len(st)-1
    while i<r:
        while not st[i].isalnum(): i+=1
        while not st[r].isalnum(): r-=1
        if st[i].lower() != st[r].lower():
            return False
        i+=1
        r-=1
    return True

def is_palindrome(s):
    # Only keep letters and numbers, then lowercase
    chars = [c.lower() for c in s if c.isalnum()]
    left, right = 0, len(chars) - 1

    while left < right:
        if chars[left] != chars[right]:
            return False
        left += 1
        right -= 1
    return True

def Reverse_String(ar):
    '''Reverse an array of characters in-place.'''
    i=0
    r=len(ar)-1
    while i<r:
        tmp = ar[r]
        ar[r] = ar[i]
        ar[i] = tmp
        i+=1
        r-=1

def reverse_string(s):
    left, right = 0, len(s) - 1
    while left < right:
        s[left], s[right] = s[right], s[left] # Pythonic swap
        left += 1
        right -= 1

def Remove_Duplicates_from_Sorted_Array(sar):
    '''Modify an array in-place to remove duplicates.'''
    i=0
    j=1
    while j<len(sar):
        if sar[i]==sar[j]:
            del sar[j]
        else:
            i+=1
            j+=1

def remove_duplicates(nums):
    if not nums: return 0
    slow = 0
    for fast in range(1, len(nums)):
        if nums[fast] != nums[slow]:
            slow += 1
            nums[slow] = nums[fast]
    return slow + 1

def Merge_Sorted_Arrays(sar1,sar2):
    '''Combine two sorted arrays into one.'''
    i=0
    j=0
    sar = []
    while i<len(sar1) and j<len(sar2):
        if sar1[i]<sar2[j]:
            sar.append(sar1[i])
            i+=1
        elif sar1[i]>sar2[j]:
            sar.append(sar2[j])
            j+=1
        else:
            sar.append(sar1[i])
            i+=1
            sar.append(sar2[j])
            j+=1
    if i<len(sar1):
        sar += sar1[i:]
    if j<len(sar2):
        sar += sar2[j:]
    return sar

def merge(nums1, m, nums2, n):
    # Fill from the back to avoid overwriting elements in nums1
    p1, p2, p = m - 1, n - 1, m + n - 1
    while p2 >= 0:
        if p1 >= 0 and nums1[p1] > nums2[p2]:
            nums1[p] = nums1[p1]
            p1 -= 1
        else:
            nums1[p] = nums2[p2]
            p2 -= 1
        p -= 1

def removeDuplicatesII(nums: List[int]) -> int:
    if not nums: return 0
    if len(nums)<3: return len(nums)
    slow = 0
    for fast in range(2, len(nums)):
        if nums[fast] != nums[slow]:
            slow += 1
            nums[slow+1] = nums[fast]
    return slow+2

def rotate( nums: List[int], k: int) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """
    n = len(nums)
    prev = nums[0:k]
    tmp=[0 for i in range(k)]
    for i in range(0,n,k):
        for j in range(k):
            tmp[j] = nums[(i+k+j)%n]
            nums[(i+k+j)%n] = prev[j]
        prev = tmp

