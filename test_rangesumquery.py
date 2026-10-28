import rangesumquery


def make(nums):
    return rangesumquery.NumArray(nums)


def test_basic_examples():
    arr = make([-2, 0, 3, -5, 2, -1])
    assert arr.sumRange(0, 2) == 1
    assert arr.sumRange(2, 5) == -1
    assert arr.sumRange(0, 5) == -3


def test_single_element_range():
    arr = make([4, 7, 9])
    assert arr.sumRange(1, 1) == 7


def test_range_starting_at_zero():
    arr = make([1, 2, 3, 4])
    assert arr.sumRange(0, 0) == 1
    assert arr.sumRange(0, 3) == 10


def test_range_ending_at_last_index():
    arr = make([1, 2, 3, 4])
    assert arr.sumRange(3, 3) == 4
    assert arr.sumRange(2, 3) == 7


def test_single_element_array():
    arr = make([5])
    assert arr.sumRange(0, 0) == 5


def test_negative_numbers():
    arr = make([-1, -2, -3])
    assert arr.sumRange(0, 2) == -6
    assert arr.sumRange(1, 2) == -5


def test_repeated_queries_give_same_answer():
    arr = make([3, 1, 4, 1, 5])
    assert arr.sumRange(1, 3) == 6
    assert arr.sumRange(1, 3) == 6


def test_many_queries_on_large_array():
    n = 10000
    nums = list(range(n))
    arr = make(nums)
    for i in range(n):
        left = i // 2
        assert arr.sumRange(left, i) == sum(range(left, i + 1))
