"""
Day 4 - LeetCode 215: Kth Largest Element in an Array (Medium)

Given an integer array nums and an integer k, return the kth LARGEST element
in the array. It is the kth largest in sorted order, not the kth distinct
element (duplicates count separately).

Example 1:  nums = [3,2,1,5,6,4],        k = 2  ->  5
Example 2:  nums = [3,2,3,1,2,4,5,5,6],  k = 4  ->  4

Constraints:
    1 <= k <= len(nums) <= 10^5
    -10^4 <= nums[i] <= 10^4

The guide's hint for this problem: a min-heap of size k. Push each number,
and whenever the heap grows past k, pop the smallest. What is left are the k
largest, and the smallest of those (heap[0]) is the kth largest.
Sorting the whole array also passes the tests; try the heap anyway, since it
is the pattern Amazon OAs like.

Run your tests with:  pytest test_kthlargest.py
"""


class Solution:
    def findKthLargest(self, nums, k):
        nums = sorted(nums, reverse=True)
        return nums[k-1]
