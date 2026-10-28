import kthlargest


def check(nums, k):
    return kthlargest.Solution().findKthLargest(nums, k)


def test_basic():
    assert check([3, 2, 1, 5, 6, 4], 2) == 5


def test_duplicates_count_separately():
    assert check([3, 2, 3, 1, 2, 4, 5, 5, 6], 4) == 4


def test_k_is_one_the_maximum():
    assert check([7, 2, 9, 4], 1) == 9


def test_k_equals_length_the_minimum():
    assert check([7, 2, 9, 4], 4) == 2


def test_single_element():
    assert check([8], 1) == 8


def test_negative_numbers():
    assert check([-1, -5, -3], 2) == -3


def test_all_equal():
    assert check([2, 2, 2, 2], 3) == 2


def test_does_not_modify_the_input():
    data = [3, 2, 1, 5, 6, 4]
    check(data, 2)
    assert data == [3, 2, 1, 5, 6, 4]


def test_large_input():
    nums = list(range(100000, 0, -1))
    assert check(nums, 1) == 100000
    assert check(nums, 100000) == 1
    assert check(nums, 50000) == 50001
