class IntervalSolutions:
    # 1. Summary Ranges
    def summaryRanges(self, nums: list[int]) -> list[str]:
        res, i = [], 0
        while i < len(nums):
            s = nums[i]
            while i + 1 < len(nums) and nums[i] + 1 == nums[i+1]:
                i += 1
            res.append(str(s) + ("->" + str(nums[i]) if s != nums[i] else ""))
            i += 1
        return res

    # 2. Merge Intervals
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        intervals.sort(key=lambda i: i[0])
        output = [intervals[0]]
        for start, end in intervals[1:]:
            lastEnd = output[-1][1]
            if start <= lastEnd:
                output[-1][1] = max(lastEnd, end)
            else:
                output.append([start, end])
        return output

    # 3. Insert Interval
    def insert(self, intervals: list[list[int]], newInterval: list[int]) -> list[list[int]]:
        res = []
        for i in range(len(intervals)):
            if newInterval[1] < intervals[i][0]:
                res.append(newInterval)
                return res + intervals[i:]
            elif newInterval[0] > intervals[i][1]:
                res.append(intervals[i])
            else:
                newInterval = [min(newInterval[0], intervals[i][0]), max(newInterval[1], intervals[i][1])]
        res.append(newInterval)
        return res

    # 4. Minimum Number of Arrows to Burst Balloons
    def findMinArrowShots(self, points: list[list[int]]) -> int:
        points.sort(key=lambda x: x[1])
        arrows, prev_end = 0, float('-inf')
        for start, end in points:
            if start > prev_end:
                arrows += 1
                prev_end = end
        return arrows
