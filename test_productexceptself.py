import productexceptself


def check(nums):
    return productexceptself.Solution().productExceptSelf(nums)


def test_basic():
    assert check([1, 2, 3, 4]) == [24, 12, 8, 6]


def test_single_zero():
    assert check([-1, 1, 0, -3, 3]) == [0, 0, 9, 0, 0]


def test_two_zeros_everything_is_zero():
    assert check([0, 4, 0]) == [0, 0, 0]


def test_two_elements():
    assert check([3, 5]) == [5, 3]


def test_negative_numbers():
    assert check([-2, -3, 4]) == [-12, -8, 6]


def test_all_ones():
    assert check([1, 1, 1, 1]) == [1, 1, 1, 1]


def test_zero_at_the_start():
    assert check([0, 2, 3]) == [6, 0, 0]


def test_zero_at_the_end():
    assert check([2, 3, 0]) == [0, 0, 6]


def test_does_not_modify_the_input():
    data = [1, 2, 3, 4]
    check(data)
    assert data == [1, 2, 3, 4]


def test_large_input():
    nums = [2, 3] + [1] * 99998
    result = check(nums)
    assert len(result) == 100000
    assert result[0] == 3
    assert result[1] == 2
    assert result[2] == 6
    assert result[-1] == 6
