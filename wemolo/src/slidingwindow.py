class SlidingWindowSolutions:
    # 1. Minimum Size Subarray Sum
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        l, total, res = 0, 0, float("inf")
        for r in range(len(nums)):
            total += nums[r]
            while total >= target:
                res = min(res, r - l + 1)
                total -= nums[l]
                l += 1
        return 0 if res == float("inf") else res

    # 2. Longest Substring Without Repeating Characters
    def lengthOfLongestSubstring(self, s: str) -> int:
        charSet = set()
        l, res = 0, 0
        for r in range(len(s)):
            while s[r] in charSet:
                charSet.remove(s[l])
                l += 1
            charSet.add(s[r])
            res = max(res, r - l + 1)
        return res

    # 3. Substring with Concatenation of All Words
    # (Requires frequency counter; omitted for brevity but follows a similar window pattern)

    # 4. Minimum Window Substring
    def minWindow(self, s: str, t: str) -> str:
        from collections import Counter
        if not t or not s: return ""
        dict_t = Counter(t)
        required = len(dict_t)
        l, r, formed = 0, 0, 0
        window_counts = {}
        ans = float("inf"), None, None
        while r < len(s):
            char = s[r]
            window_counts[char] = window_counts.get(char, 0) + 1
            if char in dict_t and window_counts[char] == dict_t[char]: formed += 1
            while l <= r and formed == required:
                char = s[l]
                if r - l + 1 < ans[0]: ans = (r - l + 1, l, r)
                window_counts[char] -= 1
                if char in dict_t and window_counts[char] < dict_t[char]: formed -= 1
                l += 1
            r += 1
        return "" if ans[0] == float("inf") else s[ans[1] : ans[2] + 1]
