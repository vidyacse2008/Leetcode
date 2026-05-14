class Solution:
    def isValid(self, s):
        matches = {')': '(', '}': '{', ']': '['}
        arr = []
        for c in s:
            if c in matches:
                if len(arr) == 0 or arr[-1] != matches[c]:
                    return False
                arr.pop()
            elif c in matches.values():
                arr.append(c)
        return len(arr) == 0