"""
Day 3 - LeetCode 560: Subarray Sum Equals K (Medium)

Given an integer array nums and an integer k, return the number of
contiguous, non-empty subarrays whose sum equals k.

Example 1:  nums = [1,1,1], k = 2   ->  2
Example 2:  nums = [1,2,3], k = 3   ->  2   ([1,2] and [3])

Constraints:
    1 <= len(nums) <= 2 * 10^4
    -1000 <= nums[i] <= 1000      (negative numbers are allowed!)
    -10^7 <= k <= 10^7

Target: n can be 2 * 10^4, so checking every start/end pair with a running sum
(O(n^2)) is too slow for the large tests. The guide's hint for this problem:
prefix sums combined with a hash map.

Run your tests with:  pytest test_subarraysumk.py
"""


class Solution:
    def subarraySum(self, nums, k):
        seen = {0:1}
        count = 0
        prefix_sum = 0
        for num in nums:
            prefix_sum += num
            count += seen.get(prefix_sum - k ,0)
            seen[prefix_sum] = seen.get(prefix_sum,0) +1
        return count