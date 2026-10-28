from separatezerosones import Solution


def zeros_left(s):
    return Solution().zerosLeft(s)


def either(s):
    return Solution().minSwapsEitherSide(s)


def test_leetcode_examples():
    assert zeros_left("101") == 1
    assert zeros_left("100") == 2
    assert zeros_left("0111") == 0


def test_already_separated():
    assert zeros_left("0011") == 0
    assert either("1100") == 0


def test_zeros_to_hop_over_several_ones():
    assert zeros_left("11000") == 6


def test_alternating():
    assert zeros_left("10101") == 3


def test_single_character():
    assert zeros_left("0") == 0
    assert zeros_left("1") == 0
    assert either("1") == 0


def test_either_side_picks_the_cheaper_target():
    assert either("100") == 0
    assert either("011") == 0
    assert either("101") == 1


def test_either_side_alternating():
    assert either("10101") == 3


def test_sum_of_both_directions_is_zeros_times_ones():
    s = "1101001"
    ones = s.count("1")
    zeros = s.count("0")
    # flipping every bit turns "0 before 1" pairs into "1 before 0" pairs
    other = zeros_left(s.translate(str.maketrans("01", "10")))
    assert zeros_left(s) + other == ones * zeros


def test_large_input():
    s = "1" * 50000 + "0" * 50000
    assert zeros_left(s) == 50000 * 50000
    assert either(s) == 0
