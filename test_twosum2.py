import twosum2


def check(numbers, target):
    return twosum2.Solution().twoSum(numbers, target)


def test_basic():
    assert check([2, 7, 11, 15], 9) == [1, 2]


def test_answer_uses_last_element():
    assert check([2, 3, 4], 6) == [1, 3]


def test_negative_numbers():
    assert check([-1, 0], -1) == [1, 2]


def test_duplicate_values():
    assert check([2, 2, 5, 6], 11) == [3, 4]


def test_same_value_twice_different_indexes():
    assert check([3, 3], 6) == [1, 2]


def test_is_one_indexed():
    result = check([1, 2, 3, 4, 5], 9)
    assert result == [4, 5]


def test_large_input():
    numbers = list(range(-1000, 1001))
    assert check(numbers, 1999) == [2000, 2001]
