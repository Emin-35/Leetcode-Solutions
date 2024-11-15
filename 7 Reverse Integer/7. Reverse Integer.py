class Solution:
    def reverse(self, x: int) -> int:
        INT_MIN = -2**31  # -2147483648
        INT_MAX = 2**31 - 1  # 2147483647
        
        sign = -1 if x < 0 else 1
        x = abs(x)
        reminder = 0

        while x != 0:
            reminder = (reminder * 10) + (x % 10)
            x //= 10  # Use integer division to avoid floating point issues
        
        reminder *= sign

        if reminder < INT_MIN or reminder > INT_MAX:
            return 0

        return reminder

def test_reverse():
    solution = Solution()

    # Test case 1: Positive number
    x = 123
    result = solution.reverse(x)
    assert result == 321, f"Expected 321, but got {result}"

    # Test case 2: Negative number
    x = -123
    result = solution.reverse(x)
    assert result == -321, f"Expected -321, but got {result}"

    # Test case 3: Single digit number (should stay the same)
    x = 5
    result = solution.reverse(x)
    assert result == 5, f"Expected 5, but got {result}"

    # Test case 4: Number with trailing zeroes (should remove leading zeros)
    x = 1200
    result = solution.reverse(x)
    assert result == 21, f"Expected 21, but got {result}"

    # Test case 5: Number that overflows the 32-bit integer range
    x = 1534236469
    result = solution.reverse(x)
    assert result == 0, f"Expected 0 (overflow), but got {result}"

    # Test case 6: Single negative digit number (should stay the same but negative)
    x = -7
    result = solution.reverse(x)
    assert result == -7, f"Expected -7, but got {result}"

    # Test case 7: Zero (should stay zero)
    x = 0
    result = solution.reverse(x)
    assert result == 0, f"Expected 0, but got {result}"

    # Test case 8: Negative number that does not overflow
    x = -456
    result = solution.reverse(x)
    assert result == -654, f"Expected -654, but got {result}"

    print("All test cases passed!")

test_reverse()
