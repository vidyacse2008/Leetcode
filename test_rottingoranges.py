import rottingoranges


def check(grid):
    return rottingoranges.Solution().orangesRotting(grid)


def test_basic():
    assert check([[2, 1, 1], [1, 1, 0], [0, 1, 1]]) == 4


def test_unreachable_fresh_orange():
    assert check([[2, 1, 1], [0, 1, 1], [1, 0, 1]]) == -1


def test_no_fresh_oranges_from_the_start():
    assert check([[0, 2]]) == 0


def test_only_empty_cells():
    assert check([[0]]) == 0


def test_single_fresh_orange_nothing_rotten():
    assert check([[1]]) == -1


def test_single_rotten_orange():
    assert check([[2]]) == 0


def test_chain_in_a_row():
    assert check([[2, 1, 1, 1]]) == 3


def test_two_sources_spread_at_the_same_time():
    assert check([[2, 1, 2]]) == 1


def test_everything_already_rotten():
    assert check([[2, 2], [2, 2]]) == 0


def test_fresh_orange_blocked_by_empty_cell():
    assert check([[2, 0, 1]]) == -1


def test_two_sources_far_apart():
    # each rotten orange reaches the middle at the same minute
    assert check([[2, 1, 1, 1, 2]]) == 2


def test_larger_grid_all_fresh_except_corner():
    grid = [[1] * 10 for _ in range(10)]
    grid[0][0] = 2
    assert check(grid) == 18
