"""
Minimum ADJACENT swaps to separate 0s and 1s (LeetCode 2938 style).

You are given a binary string s. In one step you may swap two ADJACENT
characters. Return the minimum number of steps needed to group all the 0s on one
side and all the 1s on the other side.

    zerosLeft(s)        -> 0s must end up on the LEFT, 1s on the right
                           (this is exactly LeetCode 2938)
    minSwapsEitherSide  -> either side is allowed, return the cheaper option

Examples:
    "101"   -> 1     (swap the last two: "110" has 1s left, or "011" is 1 away)
    "100"   -> 2     zerosLeft;  minSwapsEitherSide is 0 (already 1s then 0s)
    "0111"  -> 0

Idea: a swap of two adjacent characters fixes exactly one pair that is in the
wrong order. For "0s on the left", the wrong pairs are (a 1 somewhere before a 0).
Count them in one pass: keep how many 1s you have seen, and every time you meet a
0, add that count to the answer. O(n) time, O(1) space.

Run the tests with:  pytest test_separatezerosones.py
"""


class Solution:
    def zerosLeft(self, s):
        ones_seen = 0
        swaps = 0
        for ch in s:
            if ch == "1":
                ones_seen += 1
            else:
                swaps += ones_seen      # this 0 must hop over every 1 before it
        return swaps

    def minSwapsEitherSide(self, s):
        ones_seen = 0
        zeros_seen = 0
        zeros_left_cost = 0             # pairs (1 before 0)
        ones_left_cost = 0              # pairs (0 before 1)
        for ch in s:
            if ch == "1":
                ones_left_cost += zeros_seen
                ones_seen += 1
            else:
                zeros_left_cost += ones_seen
                zeros_seen += 1
        return min(zeros_left_cost, ones_left_cost)
