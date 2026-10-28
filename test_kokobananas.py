import kokobananas


def check(piles, h):
    return kokobananas.Solution().minEatingSpeed(piles, h)


def test_basic():
    assert check([3, 6, 7, 11], 8) == 4


def test_must_eat_biggest_pile_in_one_hour():
    assert check([30, 11, 23, 4, 20], 5) == 30


def test_one_spare_hour():
    assert check([30, 11, 23, 4, 20], 6) == 23


def test_single_pile():
    assert check([10], 10) == 1


def test_single_pile_one_hour():
    assert check([10], 1) == 10


def test_two_equal_piles_four_hours():
    # speed 5 -> 2 + 2 = 4 hours; speed 4 -> 3 + 3 = 6 hours
    assert check([10, 10], 4) == 5


def test_piles_of_one():
    assert check([1] * 10000, 10000) == 1


def test_huge_piles_need_huge_speed():
    # a speed-by-speed search from 1 would never finish
    assert check([10**9] * 10000, 10000) == 10**9


def test_huge_pile_lots_of_time():
    assert check([10**9], 10**9) == 1
