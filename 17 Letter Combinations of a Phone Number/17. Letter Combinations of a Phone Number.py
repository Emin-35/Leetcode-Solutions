from typing import List

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

def test_letterCombinations():
    solution = Solution()

    # Test case 1: General case
    assert solution.letterCombinations("23") == ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"], "Test case 1 failed"

    # Test case 2: Empty input string
    assert solution.letterCombinations("") == [], "Test case 2 failed"

    # Test case 3: Single digit input (2)
    assert solution.letterCombinations("2") == ["a", "b", "c"], "Test case 3 failed"

    # Test case 4: Single digit input (7)
    assert solution.letterCombinations("7") == ["p", "q", "r", "s"], "Test case 4 failed"

    # Test case 5: Larger input with multiple digits
    assert solution.letterCombinations("568") == ["jmt", "jmu", "jmv", "jnt", "jnu", "jnv", "jot", "jou", "jov", 
                                                  "kmt", "kmu", "kmv", "knt", "knu", "knv", "kot", "kou", "kov", 
                                                  "lmt", "lmu", "lmv", "lnt", "lnu", "lnv", "lot", "lou", "lov"], "Test case 5 failed"

    # Test case 6: Test digits with no corresponding letters (like 0 and 1)
    assert solution.letterCombinations("01") == [], "Test case 6 failed"

    print("All test cases passed!")

# Run the tests
test_letterCombinations()
