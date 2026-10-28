"""
Day 3 redo - LeetCode 56: Merge Intervals (Medium)

Given intervals where intervals[i] = [start, end], merge all overlapping
intervals and return the non-overlapping intervals that cover all of them.
The input is NOT guaranteed to be sorted. Intervals that only touch
(like [1,4] and [4,5]) count as overlapping.

Example 1:  [[1,3],[2,6],[8,10],[15,18]]  ->  [[1,6],[8,10],[15,18]]
Example 2:  [[1,4],[4,5]]                 ->  [[1,5]]

Constraints:
    1 <= len(intervals) <= 10^4
    intervals[i].length == 2
    0 <= start <= end <= 10^4

Goal: rewrite it from memory, without opening mergeIntervals.py.

Run your tests with:  pytest test_mergeintervalsredo.py
"""


class Solution:
    def merge(self, intervals):
        if not intervals:
          return[]
        intervals = sorted(intervals, key = lambda x: x[0])
        merged = [list(intervals[0])]
        for start,end in intervals[1:]:
           last_end = merged[-1][1]
           if start <= last_end:
              merged[-1][1] = max(last_end,end)
           else:
              merged.append([start,end])
        return merged
