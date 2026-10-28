"""
Day 4 - LeetCode 704: Binary Search (Easy)

Given an array of integers nums sorted in ascending order and an integer
target, return the index of target in nums, or -1 if it is not there.
You must write an algorithm with O(log n) runtime.

Example 1:  nums = [-1,0,3,5,9,12], target = 9  ->  4
Example 2:  nums = [-1,0,3,5,9,12], target = 2  ->  -1

Constraints:
    1 <= len(nums) <= 10^4
    -10^4 < nums[i], target < 10^4
    All the integers in nums are unique.
    nums is sorted in ascending order.

Hint from the guide: check the middle, then throw away the half that cannot
contain the answer. Write the loop by hand; do not use list.index or bisect.

Run your tests with:  pytest test_binarysearch.py
"""


class Solution:
    def search(self, nums, target):
       lo = 0
       hi = len(nums) - 1
       while lo <= hi :
           mid = (lo+hi) // 2
           if nums[mid] == target :
               return mid
           elif nums[mid] < target:
                lo = mid + 1
           else:
               hi = mid - 1
       return -1
        
               
