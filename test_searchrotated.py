import searchrotated


def check(nums, target):
    return searchrotated.Solution().search(nums, target)


def rotate(nums, r):
    return nums[r:] + nums[:r]


def test_found_after_the_pivot():
    assert check([4, 5, 6, 7, 0, 1, 2], 0) == 4


def test_not_found():
    assert check([4, 5, 6, 7, 0, 1, 2], 3) == -1


def test_single_element_not_found():
    assert check([1], 0) == -1


def test_single_element_found():
    assert check([1], 1) == 0


def test_two_elements_rotated():
    assert check([3, 1], 1) == 1
    assert check([3, 1], 3) == 0


def test_two_elements_not_rotated():
    assert check([1, 3], 3) == 1
    assert check([1, 3], 1) == 0


def test_not_rotated_at_all():
    nums = [1, 2, 3, 4, 5, 6]
    for i, value in enumerate(nums):
        assert check(nums, value) == i


def test_every_element_at_every_rotation():
    base = [2, 4, 6, 8, 10, 12, 14]
    for r in range(len(base)):
        nums = rotate(base, r)
        for i, value in enumerate(nums):
            assert check(nums, value) == i, (nums, value)


def test_missing_targets_at_every_rotation():
    base = [2, 4, 6, 8, 10, 12, 14]
    for r in range(len(base)):
        nums = rotate(base, r)
        for target in (1, 3, 7, 13, 15):
            assert check(nums, target) == -1, (nums, target)


def test_target_is_the_pivot_value():
    assert check([6, 7, 1, 2, 3, 4, 5], 1) == 2


def test_negative_numbers():
    assert check([3, 4, -5, -2, 0, 1], -2) == 3


def test_large_input():
    base = list(range(0, 10000, 2))        # 5000 sorted even numbers
    nums = rotate(base, 1234)
    for i, value in enumerate(nums):
        assert check(nums, value) == i
    assert check(nums, 1) == -1
    assert check(nums, 9999) == -1
