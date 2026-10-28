import validanagram


def check(s, t):
    return validanagram.Solution().isAnagram(s, t)


def test_anagram():
    assert check("anagram", "nagaram") is True


def test_not_anagram():
    assert check("rat", "car") is False


def test_different_lengths():
    assert check("ab", "abc") is False


def test_repeated_letters_different_counts():
    assert check("aab", "abb") is False


def test_single_char():
    assert check("a", "a") is True
