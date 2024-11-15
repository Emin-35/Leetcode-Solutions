class Solution:
    def romanToInt(self, s: str) -> int:

        roman_to_int = {
            "I": 1,
            "IV": 4,
            "V": 5,
            "IX":9,
            "X": 10,
            "XL": 40,
            "L": 50,
            "XC": 90,
            "C": 100,
            "CD": 400,
            "D": 500,
            "CM": 900,
            "M": 1000
        }

        result = 0
        i = len(s) - 1

        while i >= 0:
            if i > 0 and roman_to_int[s[i]] > roman_to_int[s[i-1]]:
                result += roman_to_int[s[i]] - roman_to_int[s[i-1]]
                i -= 2  # Skip the next character since it's already processed in the if condition
            else:
                result += roman_to_int[s[i]]
                i -= 1

        return result
    
def test_romanToInt():
    solution = Solution()

    # Test case 1: Basic Roman numeral without subtractive notation
    assert solution.romanToInt("III") == 3, "Test case 1 failed"  # 1 + 1 + 1

    # Test case 2: Roman numeral with subtractive notation
    assert solution.romanToInt("IV") == 4, "Test case 2 failed"  # 5 - 1

    # Test case 3: Combination of additive and subtractive notation
    assert solution.romanToInt("IX") == 9, "Test case 3 failed"  # 10 - 1

    # Test case 4: Standard Roman numeral
    assert solution.romanToInt("LVIII") == 58, "Test case 4 failed"  # 50 + 5 + 3

    # Test case 5: Complex Roman numeral with subtractive components
    assert solution.romanToInt("MCMXCIV") == 1994, "Test case 5 failed"  # 1000 + 900 + 90 + 4

    # Test case 6: Largest valid Roman numeral
    assert solution.romanToInt("MMMCMXCIX") == 3999, "Test case 6 failed"  # 3000 + 900 + 90 + 9

    # Test case 7: Smallest valid Roman numeral
    assert solution.romanToInt("I") == 1, "Test case 7 failed"  # 1

    # Test case 8: Mixed subtractive and additive notation
    assert solution.romanToInt("XLII") == 42, "Test case 8 failed"  # 40 + 1 + 1

    # Test case 9: Roman numeral with repeated characters
    assert solution.romanToInt("CCCLXIX") == 369, "Test case 9 failed"  # 300 + 60 + 9

    print("All test cases passed!")

# Run the tests
test_romanToInt()
