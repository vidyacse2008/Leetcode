from Longestsubstringwithoutrepeat import Solution
def test_case1_allunique():
    testword = "abc"
    expectedresult = 3
    solution = Solution()
    res = solution.length_of_longest_substr(testword)
    assert res == expectedresult
def test_case2_repeating():
    testword = "abcabc"
    expectedresult = 3
    solution = Solution()
    res = solution.length_of_longest_substr(testword)
    assert res == expectedresult
def test_case3_nounique():
    testword="aaaaaa"
    expectedresult = 1
    solution = Solution()
    res = solution.length_of_longest_substr(testword)
    assert res == expectedresult
def test_case4_singleword():
    testword="a"
    expectedresult = 1
    solution = Solution()
    res = solution.length_of_longest_substr(testword)
    assert res == expectedresult



