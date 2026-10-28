import subarraysumk


def check(nums, k):
    return subarraysumk.Solution().subarraySum(nums, k)


def test_basic():
    assert check([1, 1, 1], 2) == 2


def test_two_subarrays():
    assert check([1, 2, 3], 3) == 2


def test_with_zero_and_negative():
    # [1,-1], [1,-1,0], [0]
    assert check([1, -1, 0], 0) == 3


def test_no_match():
    assert check([1], 0) == 0


def test_single_element_match():
    assert check([5], 5) == 1


def test_negatives_only():
    assert check([-1, -1, 1], 0) == 1


def test_subarray_starting_at_index_zero_counts():
    assert check([3, 4, 7], 7) == 2


def test_large_all_zeros():
    # every non-empty subarray sums to 0: n * (n + 1) / 2
    n = 20000
    assert check([0] * n, 0) == n * (n + 1) // 2


def test_large_ones():
    assert check([1] * 20000, 1) == 20000
