import binarysearch


def check(nums, target):
    return binarysearch.Solution().search(nums, target)


def test_found():
    assert check([-1, 0, 3, 5, 9, 12], 9) == 4


def test_not_found():
    assert check([-1, 0, 3, 5, 9, 12], 2) == -1


def test_single_element_found():
    assert check([5], 5) == 0


def test_single_element_not_found():
    assert check([5], 3) == -1


def test_first_element():
    assert check([1, 3, 5, 7], 1) == 0


def test_last_element():
    assert check([1, 3, 5, 7], 7) == 3


def test_target_smaller_than_everything():
    assert check([10, 20, 30], 5) == -1


def test_target_larger_than_everything():
    assert check([10, 20, 30], 99) == -1


def test_even_length_array():
    nums = [2, 4, 6, 8]
    for i, value in enumerate(nums):
        assert check(nums, value) == i


def test_large_input_every_target():
    nums = list(range(-5000, 5000))
    for i in range(0, len(nums), 1):
        assert check(nums, nums[i]) == i
    assert check(nums, 5000) == -1
