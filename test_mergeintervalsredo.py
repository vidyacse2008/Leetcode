import mergeintervalsredo


def check(intervals):
    return mergeintervalsredo.Solution().merge(intervals)


def test_basic():
    assert check([[1, 3], [2, 6], [8, 10], [15, 18]]) == [[1, 6], [8, 10], [15, 18]]


def test_touching_intervals_merge():
    assert check([[1, 4], [4, 5]]) == [[1, 5]]


def test_unsorted_input():
    assert check([[4, 7], [1, 3], [2, 6]]) == [[1, 7]]


def test_unsorted_pair():
    assert check([[1, 4], [0, 4]]) == [[0, 4]]


def test_one_interval_inside_another():
    assert check([[1, 10], [2, 3], [4, 5]]) == [[1, 10]]


def test_single_interval():
    assert check([[1, 2]]) == [[1, 2]]


def test_no_overlap():
    assert check([[1, 2], [3, 4], [5, 6]]) == [[1, 2], [3, 4], [5, 6]]


def test_does_not_modify_the_input():
    data = [[1, 3], [2, 6]]
    check(data)
    assert data == [[1, 3], [2, 6]]


def test_large_input():
    intervals = [[i, i + 1] for i in range(10000)]
    assert check(intervals) == [[0, 10000]]
