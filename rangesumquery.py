"""
Day 3 optional - LeetCode 303: Range Sum Query - Immutable (Easy)

Design a class NumArray that is built once from an integer array nums and then
answers many queries:

    NumArray(nums)            builds the object
    sumRange(left, right)     returns the sum of nums[left..right], inclusive

Example:
    nums = [-2, 0, 3, -5, 2, -1]
    sumRange(0, 2)  ->  1    (-2 + 0 + 3)
    sumRange(2, 5)  -> -1    (3 + -5 + 2 + -1)
    sumRange(0, 5)  -> -3

Constraints:
    1 <= len(nums) <= 10^4
    -10^5 <= nums[i] <= 10^5
    0 <= left <= right < len(nums)
    At most 10^4 calls to sumRange.

Target: there can be many queries, so adding up nums[left..right] from scratch
on every call is slow. Do some work once in __init__ so that each sumRange call
is O(1).

Run your tests with:  pytest test_rangesumquery.py
"""


class NumArray:
    def __init__(self, nums):
        prefix_sum=0
        self.prefix_sum_arr=[]
        self.prefix_sum_arr.append(prefix_sum)
        for num in nums:
            prefix_sum+=num
            self.prefix_sum_arr.append(prefix_sum)

    def sumRange(self, left, right):
        return self.prefix_sum_arr[right+1] - self.prefix_sum_arr[left]
