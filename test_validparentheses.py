from validparentheses import Solution

class TestValidParentheses:
    def test_valid_simple(self):
        assert Solution().isValid("()") == True

    def test_valid_mixed(self):
        assert Solution().isValid("()[]{}") == True

    def test_invalid_wrong_order(self):
        assert Solution().isValid("({)}") == False

    def test_invalid_unclosed(self):
        assert Solution().isValid("(") == False

    def test_empty_string(self):
        assert Solution().isValid("") == True

    def test_invalid_empty_stack(self):
        assert Solution().isValid(")") == False
    def test_invalid_extra_open(self):
        assert Solution().isValid("(()") == False
    def test_invalid_extra_close(self):
        assert Solution().isValid("())") == False
    def test_valid_nested(self):
        assert Solution().isValid("{[()]}") == True
    def test_invalid_mismatched_types(self):
        assert Solution().isValid("{[(])}") == False
    def test_valid_long_string(self):
        assert Solution().isValid("((({{{[[[]]]}}})))") == True
    def test_invalid_long_string(self):
        assert Solution().isValid("((({{{[[[}}})))") == False
    def test_valid_repeated_pairs(self):
        assert Solution().isValid("()()()") == True
    def test_invalid_repeated_pairs(self):
        assert Solution().isValid("(()()") == False
    def test_valid_complex(self):
        assert Solution().isValid("({[]})(){}") == True