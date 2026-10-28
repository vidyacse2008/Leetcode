"""
Day 3 optional - LeetCode 238: Product of Array Except Self (Medium)

Given an integer array nums, return an array answer where answer[i] is the
product of ALL the elements of nums EXCEPT nums[i].

You must write an algorithm that runs in O(n) time and WITHOUT using the
division operator.

Example 1:  nums = [1,2,3,4]       ->  [24, 12, 8, 6]
Example 2:  nums = [-1,1,0,-3,3]   ->  [0, 0, 9, 0, 0]

Constraints:

    2 <= len(nums) <= 10^5
    -30 <= nums[i] <= 30
    The product of any prefix or suffix of nums fits in a 32-bit integer.

Think about it: answer[i] = (product of everything to the LEFT of i)
                          x (product of everything to the RIGHT of i).
The guide's hint for this problem: prefix / suffix.

Follow-up: can you do it with O(1) extra space, not counting the output list?

Run your tests with:  pytest test_productexceptself.py
"""


class Solution:
    def productExceptSelf(self, nums):
        n = len(nums)
        answer = [1] * n

        # pass 1: answer[i] = product of everything to the LEFT of i
        left = 1
        for i in range(n):
            answer[i] = left
            left *= nums[i]

        # pass 2: multiply in the product of everything to the RIGHT of i
        right = 1
        for i in range(n - 1, -1, -1):
            answer[i] *= right
            right *= nums[i]

        return answer
