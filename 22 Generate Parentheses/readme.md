# Question
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

Example 1:

Input: n = 3

Output: ["((()))","(()())","(())()","()(())","()()()"]

Example 2:

Input: n = 1

Output: ["()"]

# Intuition
The problem is to generate all possible valid combinations of parentheses for a given number of pairs `n`. The key insight is that a valid combination follows two basic rules:
- The number of opening parentheses `(` must always be greater than or equal to the number of closing parentheses `)` at any point in the string.
- The total number of opening and closing parentheses should both be equal to `n`.

The idea is to generate combinations recursively by trying to add an opening or closing parenthesis at each step, ensuring validity by keeping track of how many opening and closing parentheses are used.

# Approach
1. **Base Case**: If `n == 0`, return an empty list as there are no combinations possible.
2. **Recursive Function**: 
   - Use recursion to explore the possibility of adding an opening or closing parenthesis.
   - Track the number of remaining opening (`open_parenth`) and closing (`close_parenth`) parentheses.
   - Add an opening parenthesis if there are any remaining.
   - Add a closing parenthesis if it does not exceed the number of opening parentheses.
3. **Memoization**: Use `@cache` (or `lru_cache`) to store previously computed results, avoiding redundant calculations and improving efficiency.

### Result Collection:
- Collect valid combinations directly in the recursive function without maintaining a separate list.

# Complexity
- **Time Complexity**:  
  $$O(4^n / \sqrt{n})$$  
  The number of valid parentheses combinations grows exponentially, but with memoization, this is reduced significantly.

- **Space Complexity**:  
  $$O(n)$$  
  Space is used by the recursive call stack and the memoization cache.

# Code
```python3 []
from typing import List
from functools import cache

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        if n == 0:
            return []

        @cache
        def recursive(dummy_str, open_parenth, close_parenth):
            if open_parenth == close_parenth == 0:
                return [dummy_str]

            result = []
            if open_parenth > 0:
                result.extend(recursive(dummy_str + "(", open_parenth - 1, close_parenth))

            if close_parenth > open_parenth:
                result.extend(recursive(dummy_str + ")", open_parenth, close_parenth - 1))

            return result
        
        return recursive("", n, n)
```