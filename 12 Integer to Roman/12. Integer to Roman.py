class Solution:
    def intToRoman(self, num: int) -> str:
        #Create a dictionary for the roman keys and values
        roman_numbers = {
            "M": 1000,
            "CM": 900,
            "D": 500,
            "CD": 400,
            "C": 100,
            "XC": 90,
            "L": 50,
            "XL": 40,
            "X": 10,
            "IX": 9,
            "V": 5,
            "IV": 4,
            "I": 1
        }

        romans = ""

        while num > 0:
            for roman, value in roman_numbers.items():
                if num >= value:
                    romans += roman
                    num -= value
                    break  #Break the loop after adding the largest possible Roman numeral
        return romans

def test_intToRoman():
    solution = Solution()

    # Test case 1: Typical case
    assert solution.intToRoman(58) == "LVIII", "Test case 1 failed"  # 50 + 5 + 3

    # Test case 2: Number with subtractive notation
    assert solution.intToRoman(1994) == "MCMXCIV", "Test case 2 failed"  # 1000 + 900 + 90 + 4

    # Test case 3: Smallest number
    assert solution.intToRoman(1) == "I", "Test case 3 failed"

    # Test case 4: Largest single Roman numeral
    assert solution.intToRoman(1000) == "M", "Test case 4 failed"

    # Test case 5: Complex combination with different numerals
    assert solution.intToRoman(846) == "DCCCXLVI", "Test case 5 failed"  # 500 + 300 + 40 + 6

    # Test case 6: Number with multiple subtractive notations
    assert solution.intToRoman(49) == "XLIX", "Test case 6 failed"  # 40 + 9

    # Test case 7: Large number with multiple numerals
    assert solution.intToRoman(3888) == "MMMDCCCLXXXVIII", "Test case 7 failed"  # 3000 + 800 + 80 + 8

    # Test case 8: Edge of subtractive notation
    assert solution.intToRoman(3999) == "MMMCMXCIX", "Test case 8 failed"  # 3000 + 900 + 90 + 9

    print("All test cases passed!")

# Run the tests
test_intToRoman()
