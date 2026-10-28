from longestsubstringredo import Solution


def check(s):
    return Solution().lengthOfLongestSubstring(s)


def test_all_unique():
    assert check("abc") == 3


def test_repeating():
    assert check("abcabcbb") == 3


def test_all_same():
    assert check("bbbbb") == 1


def test_repeat_in_the_middle():
    assert check("pwwkew") == 3


def test_empty_string():
    assert check("") == 0


def test_single_char():
    assert check("a") == 1


def test_repeat_of_a_letter_before_the_window_start():
    # when the second 'a' arrives, the window must not move backwards
    assert check("abba") == 2


def test_spaces_and_symbols():
    assert check("a b!a") == 4


def test_large_input():
    s = "abcdefghijklmnopqrstuvwxyz" * 2000
    assert check(s) == 26
