# Question
Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent. Return the answer in any order.

A mapping of digits to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.

![1200px-telephone-keypad2svg](https://github.com/user-attachments/assets/d7608523-104c-4019-951d-f5327e0aeecc)


Example 1:

Input: digits = "23"

Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]

Example 2:

Input: digits = ""

Output: []

Example 3:

Input: digits = "2"

Output: ["a","b","c"]

# Intuition

Given a string of digits from '2' to '9', each digit can be mapped to a set of letters similar to a phone's keypad. The goal is to generate all possible letter combinations that the string of digits could represent. This problem can be solved using backtracking, where we recursively explore every possible combination by choosing one letter from the set of letters corresponding to each digit in the input string.

# Approach
1. **Base Case**: If the input string `digits` is empty, return an empty list because there are no combinations possible.
   
2. **Digit to Letter Mapping**: Create a dictionary that maps each digit ('2' to '9') to its corresponding list of letters. The mapping is as follows:
    - '2' -> ['a', 'b', 'c']
    - '3' -> ['d', 'e', 'f']
    - '4' -> ['g', 'h', 'i']
    - '5' -> ['j', 'k', 'l']
    - '6' -> ['m', 'n', 'o']
    - '7' -> ['p', 'q', 'r', 's']
    - '8' -> ['t', 'u', 'v']
    - '9' -> ['w', 'x', 'y', 'z']

3. **Backtracking**: Use a helper function (`backtrack`) to explore all possible combinations. At each step:
    - Pick a letter from the set of letters corresponding to the current digit.
    - Move to the next digit and repeat the process.
    - If we reach the end of the input string, add the current combination to the result list.

4. **Edge Cases**: If the input string contains '0' or '1', which do not map to any letters, return an empty list immediately.

# Complexity

- **Time Complexity**: 
  - Let `n` be the length of the input string `digits`.
  - For each digit, we have a constant number of letters (3 or 4). Therefore, the time complexity is `O(4^n)` in the worst case (when all digits map to 4 letters).

- **Space Complexity**: 
  - The space complexity is `O(4^n)` because we need to store all possible combinations in the result list. The recursive stack also contributes to the space complexity, but it is also `O(n)` in the worst case.

# Code
```python3 []
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        # Mapping of digits to letters
        digit_to_letters = {
            '2': ['a', 'b', 'c'],
            '3': ['d', 'e', 'f'],
            '4': ['g', 'h', 'i'],
            '5': ['j', 'k', 'l'],
            '6': ['m', 'n', 'o'],
            '7': ['p', 'q', 'r', 's'],
            '8': ['t', 'u', 'v'],
            '9': ['w', 'x', 'y', 'z']
        }
        
        # If digits contain '0' or '1', return an empty list as they don't map to any letters
        if any(digit in '01' for digit in digits):
            return []

        # Backtracking function to generate combinations
        def backtrack(index, current_combination):
            if index == len(digits):
                result.append(''.join(current_combination))
                return

            # Get the letters that the current digit can map to
            letters = digit_to_letters[digits[index]]

            # Loop through each letter and proceed to the next digit
            for letter in letters:
                current_combination.append(letter)
                backtrack(index + 1, current_combination)
                current_combination.pop()  # Backtrack

        result = []
        backtrack(0, [])
        return result
```
