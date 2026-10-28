"""
Day 3 - LeetCode 55: Jump Game (Medium)

You start at index 0 of nums. nums[i] is the MAXIMUM number of steps you can
jump forward from index i (you may jump fewer). Return True if you can reach
the last index, False otherwise.

Example 1:  nums = [2,3,1,1,4]  ->  True   (0 -> 1 -> 4)
Example 2:  nums = [3,2,1,0,4]  ->  False  (you always get stuck at index 3)

Constraints:
    1 <= len(nums) <= 10^4
    0 <= nums[i] <= 10^5

Target: trying every possible jump sequence is exponential. Think about what
single number you could carry while scanning to know if you are stuck.

Run your tests with:  pytest test_jumpgame.py
"""


class Solution:
    def canJump(self, nums):
        farthest = nums[0]
        for index,num in enumerate(nums):
            if index > farthest:
                return False
            farthest = max(farthest, index+num)
        return True
