"""
Day 1 - LeetCode 347: Top K Frequent Elements (Medium)

Given an integer array nums and an integer k, return the k most frequent
elements. You may return the answer in any order.

Example 1:  nums = [1,1,1,2,2,3], k = 2  ->  [1, 2]
Example 2:  nums = [1],           k = 1  ->  [1]

Constraints:
    1 <= len(nums) <= 10^5
    -10^4 <= nums[i] <= 10^4
    k is in the range [1, number of unique elements]
    The answer is guaranteed to be unique.

Follow-up: your algorithm's time complexity must be better than O(n log n).

Run your tests with:  pytest test_topkfrequent.py
"""


class Solution:
    def topKFrequent(self, nums, k):
        count={}
        arr=[]
        for num in nums:
            count[num] = count.get(num,0) + 1
        sorted_pairs = sorted(count.items(), key=lambda item: item[1], reverse=True)
        for key,_ in sorted_pairs:
            arr.append(key)
        return arr[:k]
