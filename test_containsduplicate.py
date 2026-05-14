from containsduplicate import Solution

solution = Solution()

def test_has_duplicate():
    nums = [1, 2, 3, 4, 5, 1]
    assert solution.containsDuplicate(nums) == True

def test_no_duplicate():
    nums = [1, 2, 3, 4, 5]
    assert solution.containsDuplicate(nums) == False

def test_empty_array():
    nums = []
    assert solution.containsDuplicate(nums) == False

def test_single_element():
    nums = [1]
    assert solution.containsDuplicate(nums) == False

def test_all_duplicates():
    nums = [2, 2, 2, 2]
    assert solution.containsDuplicate(nums) == True

def test_multiple_duplicates():
    nums = [1, 2, 3, 4, 5, 2, 3]
    assert solution.containsDuplicate(nums) == True

