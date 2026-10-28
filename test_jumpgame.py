import jumpgame


def check(nums):
    return jumpgame.Solution().canJump(nums)


def test_reachable():
    assert check([2, 3, 1, 1, 4]) is True


def test_stuck_on_a_zero():
    assert check([3, 2, 1, 0, 4]) is False


def test_single_element():
    assert check([0]) is True


def test_zero_blocks_second_element():
    assert check([0, 1]) is False


def test_zero_in_the_middle_can_be_jumped_over():
    assert check([2, 0, 0]) is True


def test_zero_at_the_end_is_fine():
    assert check([1, 1, 0]) is True


def test_big_first_jump():
    assert check([10, 0, 0, 0, 0]) is True


def test_large_reachable():
    assert check([1] * 10000) is True


def test_large_blocked_in_the_middle():
    assert check([1] * 5000 + [0] + [1] * 4999) is False
