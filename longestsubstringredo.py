"""
Day 2 redo - LeetCode 3: Longest Substring Without Repeating Characters (Medium)

Given a string s, return the length of the longest substring that contains no
repeated characters.

Example 1:  s = "abcabcbb"  ->  3   ("abc")
Example 2:  s = "bbbbb"     ->  1   ("b")
Example 3:  s = "pwwkew"    ->  3   ("wke")

Constraints:
    0 <= len(s) <= 5 * 10^4
    s consists of English letters, digits, symbols and spaces.

Goal: rewrite it from memory, without opening your first solution.

Run your tests with:  pytest test_longestsubstringredo.py
"""


class Solution:
    def lengthOfLongestSubstring(self, s):
        count={}
        l = 0
        best =0 
        for r,ch in enumerate(s):
            count[ch] = count.get(ch,0) + 1
            while count[ch] > 1:
                count[s[l]]-=1
                l+=1
            best = max(best,r-l+1)
        return best
