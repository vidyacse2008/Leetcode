"""
Reference solution for Day 4 - LeetCode 875: Koko Eating Bananas.
Your own attempt lives in kokobananas.py; this file is just for comparison.
"""


class Solution:
    def minEatingSpeed(self, piles, h):
        def can_finish(speed):
            # a pile of p bananas takes ceil(p / speed) hours
            hours = 0
            for p in piles:
                hours += (p + speed - 1) // speed
            return hours <= h

        lo, hi = 1, max(piles)        # answer is somewhere in [1, biggest pile]
        while lo < hi:
            mid = (lo + hi) // 2
            if can_finish(mid):
                hi = mid              # mid works, so try slower (keep mid as a candidate)
            else:
                lo = mid + 1          # mid is too slow, so the answer is faster
        return lo
