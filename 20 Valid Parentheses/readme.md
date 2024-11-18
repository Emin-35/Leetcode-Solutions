# Question
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.

Open brackets must be closed in the correct order.

Every close bracket has a corresponding open bracket of the same type.
 
Example 1:

Input: s = "()"

Output: true

Example 2:

Input: s = "()[]{}"

Output: true

Example 3:

Input: s = "(]"

Output: false

Example 4:

Input: s = "([])"

Output: true

# Intuition
The problem involves checking if a string containing only parentheses, brackets, and braces is valid. A valid string must have:
- Every opening symbol matched with the correct closing symbol.
- Proper nesting and order of symbols.

# Approach
1. Use a stack to track unmatched opening symbols.
2. Traverse the string:
   - Push opening symbols `(`, `[`, `{` onto the stack.
   - For closing symbols `)`, `]`, `}`:
     - If the stack is empty, the string is invalid (no matching opening symbol).
     - Otherwise, pop the top element from the stack and check if it forms a valid pair with the current symbol.
     - If not, the string is invalid.
3. After traversal, if the stack is not empty, there are unmatched opening symbols, so the string is invalid.
4. Return `True` if valid, otherwise `False`.

# Complexity
- **Time complexity:**  $$O(n)$$  
    - Each character in the string is processed once.

- **Space complexity:**  $$O(n)$$
    - In the worst case, all characters in the string could be opening symbols stored in the stack.

# Code
```python3 []
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
```