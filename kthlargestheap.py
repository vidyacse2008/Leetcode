"""
Day 4 redo - LeetCode 215: Kth Largest Element in an Array (Medium), HEAP version

Same problem as kthlargest.py: return the kth LARGEST element of nums
(duplicates count separately).

Example 1:  nums = [3,2,1,5,6,4],        k = 2  ->  5
Example 2:  nums = [3,2,3,1,2,4,5,5,6],  k = 4  ->  4

Constraints:
    1 <= k <= len(nums) <= 10^5
    -10^4 <= nums[i] <= 10^4

Goal: do NOT sort the whole array. Use a min-heap that never holds more than
k numbers (heapq.heappush / heapq.heappop). When it grows past k, pop the
smallest. When you are done, the heap holds the k largest numbers, and the
smallest of them (heap[0]) is the kth largest.

Complexity to aim for: O(n log k) time, O(k) space.

Run your tests with:  pytest test_kthlargestheap.py
"""

import heapq
class Solution:    
    def findKthLargest(self, nums, k):
        heap=[]
        for num in nums:
            heapq.heappush(heap,num)
            if len(heap) > k :
                heapq.heappop(heap)
        return heap[0]
