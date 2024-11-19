from typing import List
from functools import cache
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        if n == 0:
            return []

        parenthesis_list = []
        @cache
        def recursive(dummy_str, open_parenth, close_parenth):
            if open_parenth == close_parenth == 0:
                parenthesis_list.append(dummy_str)
                return

            if open_parenth > 0:
                recursive(dummy_str + "(", open_parenth - 1, close_parenth)

            if close_parenth > open_parenth:
                recursive(dummy_str + ")", open_parenth, close_parenth - 1)
        
        recursive("", n, n)
        return parenthesis_list

def test_generateParenthesis():
    solution = Solution()
    
    # Test case 1: n = 0 (edge case)
    assert solution.generateParenthesis(0) == [], "Test case 1 failed"

    # Test case 2: n = 1
    assert solution.generateParenthesis(1) == ["()"], "Test case 2 failed"

    # Test case 3: n = 2
    assert solution.generateParenthesis(2) == ["(())", "()()"], "Test case 3 failed"

    # Test case 4: n = 3
    assert solution.generateParenthesis(3) == ["((()))", "(()())", "(())()", "()(())", "()()()"], "Test case 4 failed"

    # Test case 5: n = 4
    assert solution.generateParenthesis(4) == [
        "(((())))", "((()()))", "((())())", "((()))()", "(()(()))", 
        "(()()())", "(()())()", "(())(())", "(())()()", "()((()))", 
        "()(()())", "()(())()", "()()(())", "()()()()"
    ], "Test case 5 failed"

    print("All test cases passed!")

# Run test cases
test_generateParenthesis()
