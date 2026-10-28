"""
Day 4 - LeetCode 875: Koko Eating Bananas (Medium)

Koko has piles of bananas; piles[i] is the size of pile i. The guards come back
in h hours. Each hour Koko picks ONE pile and eats k bananas from it. If the
pile has fewer than k bananas she eats them all and does NOT start another pile
that hour.

Return the MINIMUM integer eating speed k so that she finishes all the piles
within h hours.

Example 1:  piles = [3,6,7,11],      h = 8  ->  4
Example 2:  piles = [30,11,23,4,20], h = 5  ->  30
Example 3:  piles = [30,11,23,4,20], h = 6  ->  23

Constraints:
    1 <= len(piles) <= 10^4
    len(piles) <= h <= 10^9
    1 <= piles[i] <= 10^9

Target: the speed can be as large as 10^9, so trying every speed from 1 upward
is too slow. This is "minimum X such that it is possible": binary search on
the ANSWER. Write a helper that checks whether a given speed works, then
search over the possible speeds.

Run your tests with:  pytest test_kokobananas.py
"""

import math
class Solution:
    def minEatingSpeed(self, piles, h):
        lo = 1
        hi = max(piles)
        while lo < hi:
            hours=0
            mid = (lo+hi)//2
            for p in piles:
                hours+= math.ceil(p / mid)
            if hours <= h:
                hi = mid
            else:
                lo = mid+1
        return lo
        
