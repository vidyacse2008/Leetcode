"""
Reference solution for Day 4 optional - LeetCode 33: Search in Rotated Sorted Array.
Your own attempt lives in searchrotated.py; this file is just for comparison.
"""


class Solution:
    def search(self, nums, target):
        lo, hi = 0, len(nums) - 1
        while lo <= hi:
            mid = (lo + hi) // 2
            if nums[mid] == target:
                return mid
            if nums[lo] <= nums[mid]:               # left half [lo..mid] is sorted
                if nums[lo] <= target < nums[mid]:  # target is inside the sorted half
                    hi = mid - 1
                else:
                    lo = mid + 1
            else:                                   # right half [mid..hi] is sorted
                if nums[mid] < target <= nums[hi]:  # target is inside the sorted half
                    lo = mid + 1
                else:
                    hi = mid - 1
        return -1
