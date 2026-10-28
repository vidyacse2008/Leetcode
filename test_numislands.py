import numislands


def check(grid):
    return numislands.Solution().numIslands(grid)


def test_one_big_island():
    grid = [["1", "1", "1", "1", "0"],
            ["1", "1", "0", "1", "0"],
            ["1", "1", "0", "0", "0"],
            ["0", "0", "0", "0", "0"]]
    assert check(grid) == 1


def test_three_islands():
    grid = [["1", "1", "0", "0", "0"],
            ["1", "1", "0", "0", "0"],
            ["0", "0", "1", "0", "0"],
            ["0", "0", "0", "1", "1"]]
    assert check(grid) == 3


def test_no_land():
    assert check([["0", "0"], ["0", "0"]]) == 0


def test_all_land():
    assert check([["1", "1"], ["1", "1"]]) == 1


def test_single_cell_land():
    assert check([["1"]]) == 1


def test_single_cell_water():
    assert check([["0"]]) == 0


def test_diagonal_does_not_connect():
    grid = [["1", "0"],
            ["0", "1"]]
    assert check(grid) == 2


def test_snake_shaped_island_is_one():
    grid = [["1", "1", "1"],
            ["0", "0", "1"],
            ["1", "1", "1"],
            ["1", "0", "0"],
            ["1", "1", "1"]]
    assert check(grid) == 1


def test_single_row():
    assert check([["1", "0", "1", "1", "0", "1"]]) == 3


def test_single_column():
    assert check([["1"], ["1"], ["0"], ["1"]]) == 2


def test_large_all_land_is_one_island():
    grid = [["1"] * 300 for _ in range(300)]
    assert check(grid) == 1


def test_large_checkerboard():
    grid = [["1" if (r + c) % 2 == 0 else "0" for c in range(300)] for r in range(300)]
    assert check(grid) == 45000
