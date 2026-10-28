"""
Day 1 - LeetCode 242: Valid Anagram (Easy)

Given two strings s and t, return True if t is an anagram of s, False otherwise.
An anagram uses exactly the same letters, the same number of times, in any order.

Example 1:  s = "anagram", t = "nagaram"  ->  True
Example 2:  s = "rat",     t = "car"      ->  False

Constraints:
    1 <= len(s), len(t) <= 5 * 10^4
    s and t consist of lowercase English letters.

Run your tests with:  pytest test_validanagram.py
"""

class Solution:
    def isAnagram(self, s, t):
        if len(s) != len(t):
            return False
        count={}
        for char in s:
            if char in count:
              count[char]+=1
            else:
                count[char] = 1
        for char in t:
                if char in count:
                    count[char]-=1
        return all(value == 0 for value in count.values())
