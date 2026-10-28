import topkfrequent


def check(nums, k):
    return sorted(topkfrequent.Solution().topKFrequent(nums, k))


def test_basic():
    assert check([1, 1, 1, 2, 2, 3], 2) == [1, 2]


def test_single_element():
    assert check([1], 1) == [1]


def test_negative_numbers():
    assert check([-1, -1, -2, -2, -2, 3], 2) == [-2, -1]


def test_k_equals_unique_count():
    assert check([4, 4, 5, 6], 3) == [4, 5, 6]


def test_large_input():
    nums = [7] * 50000 + [8] * 30000 + list(range(100, 120000 - 80000 + 100))
    assert check(nums, 2) == [7, 8]
