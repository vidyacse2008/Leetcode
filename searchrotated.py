"""
Day 4 optional - LeetCode 33: Search in Rotated Sorted Array (Medium)

nums was sorted in ascending order (all values distinct) and then ROTATED at
some unknown pivot, so for example [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2].
Given the rotated array and a target, return the index of target, or -1 if it
is not there. You must write an algorithm with O(log n) runtime.

Example 1:  nums = [4,5,6,7,0,1,2], target = 0  ->  4
Example 2:  nums = [4,5,6,7,0,1,2], target = 3  ->  -1
Example 3:  nums = [1],             target = 0  ->  -1

Constraints:
    1 <= len(nums) <= 5000
    -10^4 <= nums[i] <= 10^4
    All values of nums are unique.
    nums is an ascending array that is possibly rotated (rotation may be 0).
    -10^4 <= target <= 10^4

Hint from the guide: "modified binary search". At every step, after you pick
mid, at least ONE of the two halves [lo..mid] and [mid..hi] is still perfectly
sorted. Work out how to tell which half that is, and whether the target can be
inside it. Do not use list.index or a linear scan.

Run your tests with:  pytest test_searchrotated.py
"""


class Solution:
    def search(self, nums, target):
        lo = 0
        hi = len(nums) - 1
        while lo <= hi :
            mid = (lo + hi)//2
            if nums[mid] == target:
                return mid
            if nums[lo] <= nums[mid]:
                if nums[lo] <= target < nums[mid]:
                    hi = mid -1 
                else:
                     lo = mid+1
            else:
                if nums[mid] < target <= nums[hi]:
                    lo = mid+1
                else:
                    hi = mid-1

        return -1
