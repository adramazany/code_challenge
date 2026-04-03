class TwoPointersSolutions:
    # 1. Valid Palindrome
    def isPalindrome(self, s: str) -> bool:
        s = "".join(filter(str.isalnum, s)).lower()
        return s == s[::-1]

    # 2. Is Subsequence
    def isSubsequence(self, s: str, t: str) -> bool:
        i, j = 0, 0
        while i < len(s) and j < len(t):
            if s[i] == t[j]: i += 1
            j += 1
        return i == len(s)

    # 3. Two Sum II - Input Array Is Sorted
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        l, r = 0, len(numbers) - 1
        while l < r:
            s = numbers[l] + numbers[r]
            if s == target: return [l + 1, r + 1]
            if s < target: l += 1
            else: r -= 1

    # 4. Container With Most Water
    def maxArea(self, height: list[int]) -> int:
        l, r, res = 0, len(height) - 1, 0
        while l < r:
            res = max(res, min(height[l], height[r]) * (r - l))
            if height[l] < height[r]: l += 1
            else: r -= 1
        return res

    # 5. 3Sum
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        res = []
        for i, a in enumerate(nums):
            if i > 0 and a == nums[i-1]: continue
            l, r = i + 1, len(nums) - 1
            while l < r:
                s = a + nums[l] + nums[r]
                if s > 0: r -= 1
                elif s < 0: l += 1
                else:
                    res.append([a, nums[l], nums[r]])
                    l += 1
                    while l < r and nums[l] == nums[l-1]: l += 1
        return res
