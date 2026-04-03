class ArrayStringSolutions:
    # 1. Merge Sorted Array
    def merge(self, nums1, m, nums2, n):
        while m > 0 and n > 0:
            if nums1[m-1] > nums2[n-1]:
                nums1[m+n-1] = nums1[m-1]
                m -= 1
            else:
                nums1[m+n-1] = nums2[n-1]
                n -= 1
        nums1[:n] = nums2[:n]

    # 2. Remove Element
    def removeElement(self, nums, val):
        k = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[k] = nums[i]
                k += 1
        return k

    # 3. Remove Duplicates from Sorted Array
    def removeDuplicates(self, nums):
        if not nums: return 0
        k = 1
        for i in range(1, len(nums)):
            if nums[i] != nums[i-1]:
                nums[k] = nums[i]
                k += 1
        return k

    # 4. Remove Duplicates from Sorted Array II (At most twice)
    def removeDuplicates2(self, nums):
        k = 0
        for n in nums:
            if k < 2 or n != nums[k-2]:
                nums[k] = n
                k += 1
        return k

    # 5. Majority Element
    def majorityElement(self, nums):
        cand, count = None, 0
        for n in nums:
            if count == 0: cand = n
            count += (1 if n == cand else -1)
        return cand

    # 6. Rotate Array
    def rotate(self, nums, k):
        k %= len(nums)
        nums[:] = nums[-k:] + nums[:-k]

    # 7. Best Time to Buy and Sell Stock
    def maxProfit(self, prices):
        min_p, max_f = float('inf'), 0
        for p in prices:
            min_p = min(min_p, p)
            max_f = max(max_f, p - min_p)
        return max_f

    # 8. Best Time to Buy and Sell Stock II
    def maxProfit2(self, prices):
        return sum(max(0, prices[i] - prices[i-1]) for i in range(1, len(prices)))

    # 9. Jump Game
    def canJump(self, nums):
        gas = 0
        for n in nums:
            if gas < 0: return False
            gas = max(gas, n)
            gas -= 1
        return True

    # 10. Jump Game II
    def jump(self, nums):
        ans, end, far = 0, 0, 0
        for i in range(len(nums) - 1):
            far = max(far, i + nums[i])
            if i == end:
                ans += 1
                end = far
        return ans

    # 11. H-Index
    def hIndex(self, citations):
        citations.sort(reverse=True)
        for i, c in enumerate(citations):
            if i >= c: return i
        return len(citations)

    # 12. Insert Delete GetRandom O(1)
    # (Requires a class structure with a dict and list)

    # 13. Product of Array Except Self
    def productExceptSelf(self, nums):
        res = [1] * len(nums)
        prefix = suffix = 1
        for i in range(len(nums)):
            res[i] = prefix
            prefix *= nums[i]
        for i in range(len(nums)-1, -1, -1):
            res[i] *= suffix
            suffix *= nums[i]
        return res

    # 14. Gas Station
    def canCompleteCircuit(self, gas, cost):
        if sum(gas) < sum(cost): return -1
        total, start = 0, 0
        for i in range(len(gas)):
            total += (gas[i] - cost[i])
            if total < 0:
                total = 0
                start = i + 1
        return start

    # 15. Candy
    def candy(self, ratings):
        n = len(ratings)
        res = [1] * n
        for i in range(1, n):
            if ratings[i] > ratings[i-1]: res[i] = res[i-1] + 1
        for i in range(n-2, -1, -1):
            if ratings[i] > ratings[i+1]: res[i] = max(res[i], res[i+1] + 1)
        return sum(res)

    # 16. Trapping Rain Water
    def trap(self, height):
        l, r = 0, len(height) - 1
        l_max, r_max = 0, 0
        res = 0
        while l < r:
            if height[l] < height[r]:
                if height[l] >= l_max: l_max = height[l]
                else: res += l_max - height[l]
                l += 1
            else:
                if height[r] >= r_max: r_max = height[r]
                else: res += r_max - height[r]
                r -= 1
        return res

    # 17. Roman to Integer
    def romanToInt(self, s):
        d = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        res, prev = 0, 0
        for char in s[::-1]:
            curr = d[char]
            if curr < prev: res -= curr
            else: res += curr
            prev = curr
        return res

    # 18. Integer to Roman
    def intToRoman(self, num):
        syms = [["I", 1], ["IV", 4], ["V", 5], ["IX", 9], ["X", 10], ["XL", 40], ["L", 50], ["XC", 90], ["C", 100], ["CD", 400], ["D", 500], ["CM", 900], ["M", 1000]]
        res = ""
        for sym, val in reversed(syms):
            if num // val:
                res += (sym * (num // val))
                num %= val
        return res

    # 19. Length of Last Word
    def lengthOfLastWord(self, s):
        return len(s.split().pop())

    # 20. Longest Common Prefix
    def longestCommonPrefix(self, strs):
        if not strs: return ""
        shortest = min(strs, key=len)
        for i, char in enumerate(shortest):
            for other in strs:
                if other[i] != char:
                    return shortest[:i]
        return shortest

    # 21. Reverse Words in a String
    def reverseWords(self, s):
        return " ".join(s.split()[::-1])

    # 22. Zigzag Conversion
    def convert(self, s, numRows):
        if numRows == 1: return s
        rows = [""] * numRows
        idx, step = 0, 1
        for char in s:
            rows[idx] += char
            if idx == 0: step = 1
            elif idx == numRows - 1: step = -1
            idx += step
        return "".join(rows)

    # 23. Find the Index of the First Occurrence in a String
    def strStr(self, haystack, needle):
        return haystack.find(needle)

    # 24. Text Justification
    # (Omitted due to complexity; usually requires a helper function)
