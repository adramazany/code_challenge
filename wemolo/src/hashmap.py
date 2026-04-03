import collections

class HashmapSolutions:
    # 1. Ransom Note
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        counts = collections.Counter(magazine)
        for char in ransomNote:
            if counts[char] <= 0: return False
            counts[char] -= 1
        return True

    # 2. Isomorphic Strings
    def isIsomorphic(self, s: str, t: str) -> bool:
        return len(set(zip(s, t))) == len(set(s)) == len(set(t))

    # 3. Word Pattern
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split()
        if len(pattern) != len(words): return False
        return len(set(zip(pattern, words))) == len(set(pattern)) == len(set(words))

    # 4. Valid Anagram
    def isAnagram(self, s: str, t: str) -> bool:
        return collections.Counter(s) == collections.Counter(t)

    # 5. Group Anagrams
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        ans = collections.defaultdict(list)
        for s in strs:
            ans[tuple(sorted(s))].append(s)
        return list(ans.values())

    # 6. Two Sum
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        prevMap = {} # val : index
        for i, n in enumerate(nums):
            diff = target - n
            if diff in prevMap: return [prevMap[diff], i]
            prevMap[n] = i

    # 7. Happy Number
    def isHappy(self, n: int) -> bool:
        visit = set()
        while n not in visit:
            visit.add(n)
            n = sum(int(i)**2 for i in str(n))
            if n == 1: return True
        return False

    # 8. Contains Duplicate II
    def containsNearbyDuplicate(self, nums: list[int], k: int) -> bool:
        window = {} # val : index
        for i, n in enumerate(nums):
            if n in window and i - window[n] <= k: return True
            window[n] = i
        return False

    # 9. Longest Consecutive Sequence
    def longestConsecutive(self, nums: list[int]) -> int:
        numSet = set(nums)
        longest = 0
        for n in nums:
            if (n - 1) not in numSet:
                length = 0
                while (n + length) in numSet:
                    length += 1
                longest = max(length, longest)
        return longest
