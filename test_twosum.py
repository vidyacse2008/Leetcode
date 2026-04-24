import unittest
from twosum import Solution

class TestTwoSum(unittest.TestCase):

    def test_basic(self):
        nums = [2, 7, 11, 15]
        target = 9
        expected_result = (0, 1)
        solution = Solution()
        result = solution.twoSum(nums, target)
        self.assertEqual(result, expected_result)

    def test_duplicate_numbers(self):
        nums = [3, 3, 4]
        target = 6
        expected_result = (0,1)
        solution = Solution()
        result = solution.twoSum(nums, target)
        self.assertEqual(result, expected_result)

    def test_negative_numbers(self):
        nums = [-1, -2, -3, -4, -5]
        target = -8
        expected_result = (2, 4)
        solution = Solution()
        result = solution.twoSum(nums, target)
        self.assertEqual(result, expected_result)
    def test_no_solution(self):
        nums = [1, 2, 3]
        target = 7
        expected_result = None
        solution = Solution()
        result = solution.twoSum(nums, target)
        self.assertEqual(result, expected_result)
    def test_large_numbers(self):
        nums = [1000000000, 2000000000, 3000000000]
        target = 5000000000
        expected_result = (1, 2)
        solution = Solution()
        result = solution.twoSum(nums, target)
        self.assertEqual(result, expected_result)
    def test_same_number_twice(self):
        nums = [1, 2, 3, 4, 5]
        target = 10
        expected_result = None
        solution = Solution()
        result = solution.twoSum(nums, target)
        self.assertEqual(result, expected_result)
    def test_empty_array(self):
        nums = []
        target = 5
        expected_result = None
        solution = Solution()
        result = solution.twoSum(nums, target)
        self.assertEqual(result, expected_result)
    def test_single_element(self):
        nums = [5]
        target = 5
        expected_result = None
        solution = Solution()
        result = solution.twoSum(nums, target)
        self.assertEqual(result, expected_result)
    def test_multiple_solutions(self):
        nums = [1, 2, 3, 4, 5]
        target = 5
        expected_result = (1, 2)  # First valid pair (2 + 3)
        solution = Solution()
        result = solution.twoSum(nums, target)
        self.assertEqual(result, expected_result)
    def test_zero_target(self):
        nums = [0, 1, 2, 3, 4]
        target = 0
        expected_result = None
        solution = Solution()
        result = solution.twoSum(nums, target)
        self.assertEqual(result, expected_result)
    def test_all_zeros(self):
        nums = [0, 0, 0, 0]
        target = 0
        expected_result = (0, 1)  # First valid pair (0 + 0)
        solution = Solution()
        result = solution.twoSum(nums, target)
        self.assertEqual(result, expected_result)
    def test_large_input(self):
        nums = list(range(100000))
        target = 199997
        expected_result = (99998, 99999)  # Last two numbers (99998 + 99999)
        solution = Solution()
        result = solution.twoSum(nums, target)
        self.assertEqual(result, expected_result)
    def test_same_number_twice_not_valid(self):
        nums = [1, 2, 3, 4, 5]
        target = 2
        expected_result = None
        solution = Solution()
        result = solution.twoSum(nums, target)
        self.assertEqual(result, expected_result)
    def test_large_numbers_no_solution(self):
        nums = [1000000000, 2000000000, 3000000000]
        target = 6000000000
        expected_result = None
        solution = Solution()
        result = solution.twoSum(nums, target)
        self.assertEqual(result, expected_result)
    def test_negative_target(self):
        nums = [-1, -2, -3, -4, -5]
        target = -10
        expected_result = None
        solution = Solution()
        result = solution.twoSum(nums, target)
        self.assertEqual(result, expected_result)
    def test_mixed_numbers(self):
        nums = [-1, 0, 1, 2, -1, -4]
        target = 0
        expected_result = (0, 2)  # First valid pair (-1 + 1)
        solution = Solution()
        result = solution.twoSum(nums, target)
        self.assertEqual(result, expected_result)   
    def test_large_input_no_solution(self):
        nums = list(range(100000))
        target = 200000
        expected_result = None
        solution = Solution()
        result = solution.twoSum(nums, target)
        self.assertEqual(result, expected_result)
    def test_all_same_numbers(self):
        nums = [2, 2, 2, 2]
        target = 4
        expected_result = (0, 1)  # First valid pair (2 + 2)
        solution = Solution()
        result = solution.twoSum(nums, target)
        self.assertEqual(result, expected_result)
    def test_no_valid_pairs(self):
        nums = [1, 2, 3, 4, 5]
        target = 10
        expected_result = None
        solution = Solution()
        result = solution.twoSum(nums, target)
        self.assertEqual(result, expected_result)
    def test_large_numbers_with_duplicates(self):
        nums = [1000000000, 2000000000, 3000000000, 1000000000]
        target = 4000000000
        expected_result = (0, 2)  # First valid pair (1000000000 + 3000000000)
        solution = Solution()
        result = solution.twoSum(nums, target)
        self.assertEqual(result, expected_result)
    def test_negative_numbers_no_solution(self):
        nums = [-1, -2, -3, -4, -5]
        target = -15
        expected_result = None
        solution = Solution()
        result = solution.twoSum(nums, target)
        self.assertEqual(result, expected_result)
    def test_zero_target_with_zeros(self):
        nums = [0, 0, 0, 0]
        target = 0
        expected_result = (0, 1)  # First valid pair (0 + 0)
        solution = Solution()
        result = solution.twoSum(nums, target)
        self.assertEqual(result, expected_result)
    def test_zero_target_no_zeros(self):
        nums = [1, 2, 3, 4, 5]
        target = 0
        expected_result = None
        solution = Solution()
        result = solution.twoSum(nums, target)
        self.assertEqual(result, expected_result)
    def test_single_pair(self):
        nums = [1, 2]
        target = 3
        expected_result = (0, 1)
        solution = Solution()
        result = solution.twoSum(nums, target)
        self.assertEqual(result, expected_result)
    def test_single_pair_no_solution(self):
        nums = [1, 2]
        target = 4
        expected_result = None
        solution = Solution()
        result = solution.twoSum(nums, target)
        self.assertEqual(result, expected_result)
    