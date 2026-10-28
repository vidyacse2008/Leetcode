import besttimetobuyandsellstock


def check(prices):
    return besttimetobuyandsellstock.Solution().maxProfit(prices)


def test_basic():
    assert check([7, 1, 5, 3, 6, 4]) == 5


def test_prices_only_fall():
    assert check([7, 6, 4, 3, 1]) == 0


def test_single_day():
    assert check([5]) == 0


def test_two_days_profit():
    assert check([1, 2]) == 1


def test_lowest_price_is_after_best_sell():
    # the global minimum (0) comes last, so it can't be the buy day
    assert check([3, 10, 1, 2, 0]) == 7


def test_all_equal():
    assert check([4, 4, 4, 4]) == 0


def test_large_input():
    prices = list(range(100000))
    assert check(prices) == 99999


def check_days(prices):
    return besttimetobuyandsellstock.Solution().maxProfitDays(prices)


def test_days_basic():
    assert check_days([7, 1, 5, 3, 6, 4]) == (1, 4)


def test_days_global_min_comes_after_best_trade():
    assert check_days([3, 10, 1, 2, 0]) == (0, 1)


def test_days_no_profit():
    assert check_days([7, 6, 4, 3, 1]) == (-1, -1)


def test_days_single_day():
    assert check_days([5]) == (-1, -1)


def test_days_always_rising():
    assert check_days([1, 2, 3, 4, 5]) == (0, 4)


def test_days_tie_returns_earliest():
    # (0,1), (0,3) and (2,3) all give profit 4; the earliest trade wins
    assert check_days([1, 5, 1, 5]) == (0, 1)
