class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for c in s:
            if c in "([{":
                stack.append(c)
            elif c in ")]}":
                if len(stack) == 0:
                    return False
                else:
                    top = stack.pop()
                    if not ((top == '(' and c == ')') or
                            (top == '[' and c == ']') or
                            (top == '{' and c == '}')):
                        return False
        return len(stack) == 0

def test_isValid():
    solution = Solution()

    # Test case 1: Balanced parentheses
    assert solution.isValid("()") == True, "Test case 1 failed"

    # Test case 2: Mixed balanced brackets
    assert solution.isValid("()[]{}") == True, "Test case 2 failed"

    # Test case 3: Nested brackets
    assert solution.isValid("{[()]}") == True, "Test case 3 failed"

    # Test case 4: Unmatched closing bracket
    assert solution.isValid("(]") == False, "Test case 4 failed"

    # Test case 5: Unmatched opening bracket
    assert solution.isValid("([)") == False, "Test case 5 failed"

    # Test case 6: Empty string
    assert solution.isValid("") == True, "Test case 6 failed"

    # Test case 7: Extra opening bracket
    assert solution.isValid("(()") == False, "Test case 7 failed"

    # Test case 8: Extra closing bracket
    assert solution.isValid("())") == False, "Test case 8 failed"

    # Test case 9: Long valid string
    assert solution.isValid("({[(){}]})") == True, "Test case 9 failed"

    print("All test cases passed!")

# Run the tests
test_isValid()
