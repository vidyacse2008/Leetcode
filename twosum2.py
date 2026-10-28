"""
Day 2 - LeetCode 167: Two Sum II - Input Array Is Sorted (Medium)

numbers is sorted in non-decreasing order. Find two numbers that add up to
target. Return their positions as [index1, index2], 1-INDEXED, with
index1 < index2. Exactly one solution exists, and you may not use the same
element twice.

Your solution must use only constant extra space.

Example 1:  numbers = [2,7,11,15], target = 9   ->  [1, 2]
Example 2:  numbers = [2,3,4],     target = 6   ->  [1, 3]
Example 3:  numbers = [-1,0],      target = -1  ->  [1, 2]

Constraints:
    2 <= len(numbers) <= 3 * 10^4
    -1000 <= numbers[i] <= 1000
    numbers is sorted in non-decreasing order
    -1000 <= target <= 1000

Run your tests with:  pytest test_twosum2.py
"""


class Solution:
    def twoSum(self, numbers, target):
        l =0 
        r = len(numbers) -1 
        while l < r:
            sum = numbers[l] + numbers[r]
            if sum == target:
                return [l+1,r+1]
            elif sum < target:
                l+=1
            else:
                r-=1
        
