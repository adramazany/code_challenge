from typing import List

class Solution:

    def maxProfit(self, prices: List[int]) -> int:
        return sum(max(0,prices[i]-prices[i-1]) for i in range(1,len(prices)))

    def canJump(self, nums: List[int]) -> bool:
        gas = 0
        for n in nums:
            if gas < 0 : return False
            gas = max(n,gas)-1
        return True


    def hIndex(self, citations: List[int]) -> int:
        citations.sort(reverse=True)
        for i,c in enumerate(citations):
            if i>=c: return i
        return len(citations)

    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * len(nums)
        prefix = suffix = 1
        for i in range(len(nums)):
            res[i] = prefix
            prefix *= nums[i]
        for i in range(len(nums)-1, -1, -1):
            res[i] *= suffix
            suffix *= nums[i]
        return res

    def candy(self, ratings: List[int]) -> int:
        res = [1]*len(ratings)
        for i in range(1,len(ratings)):
            if ratings[i]>ratings[i-1]:
                res[i]=res[i-1]+1
        for i in range(len(ratings)-2,-1,-1):
            if ratings[i]>ratings[i+1]:
                res[i] = max(res[i], res[i+1]+1)
        return sum(res)