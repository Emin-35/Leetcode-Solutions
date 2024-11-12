class Solution:
    def longestPalindrome(self, s: str) -> str:
        curr = 1
        longest_str = ""

        if len(s) <= 1:
            return s

        # Check for odd-length palindromes
        while curr < len(s):
            left = curr - 1
            right = curr + 1
            dummy_str = s[curr]

            while left >= 0 and right < len(s) and s[left] == s[right]:
                dummy_str = s[left] + dummy_str + s[right]
                longest_str = max(longest_str, dummy_str, key=len)
                left -= 1
                right += 1

            curr += 1

        # Reset curr for even-length palindromes
        curr = 1

        # Check for even-length palindromes
        while curr < len(s):
            left = curr - 1
            right = curr

            dummy_str = ""
            while left >= 0 and right < len(s) and s[left] == s[right]:
                dummy_str = s[left] + dummy_str + s[right]
                longest_str = max(longest_str, dummy_str, key=len)
                left -= 1
                right += 1

            curr += 1

        return longest_str if longest_str else s[0]

def test_longestPalindrome():
    solution = Solution()

    # Test case 1: Standard case with odd-length palindrome
    s = "babad"
    result = solution.longestPalindrome(s)
    assert result in ["bab", "aba"], f"Expected 'bab' or 'aba', but got {result}"

    # Test case 2: Entire string is a palindrome
    s = "racecar"
    result = solution.longestPalindrome(s)
    assert result == "racecar", f"Expected 'racecar', but got {result}"

    # Test case 3: String with even-length palindrome
    s = "cbbd"
    result = solution.longestPalindrome(s)
    assert result == "bb", f"Expected 'bb', but got {result}"

    # Test case 4: Single character string
    s = "a"
    result = solution.longestPalindrome(s)
    assert result == "a", f"Expected 'a', but got {result}"

    # Test case 5: String with no repeating characters
    s = "abcdefg"
    result = solution.longestPalindrome(s)
    assert result in list(s), f"Expected one of the characters in '{s}', but got {result}"

    # Test case 6: Palindrome in the middle
    s = "abacdfgdcaba"
    result = solution.longestPalindrome(s)
    assert result == "aba", f"Expected 'aba', but got {result}"

    # Test case 7: Palindrome at the beginning
    s = "aabcdcb"
    result = solution.longestPalindrome(s)
    assert result == "bcdcb", f"Expected 'bcdcb', but got {result}"

    # Test case 8: Palindrome at the end
    s = "abcddcba"
    result = solution.longestPalindrome(s)
    assert result == "abcddcba", f"Expected 'abcddcba', but got {result}"

    # Test case 9: Empty string
    s = ""
    result = solution.longestPalindrome(s)
    assert result == "", f"Expected '', but got {result}"

    # Test case 10: String with multiple same-length palindromes
    s = "aabb"
    result = solution.longestPalindrome(s)
    assert result in ["aa", "bb"], f"Expected 'aa' or 'bb', but got {result}"

    print("All test cases passed!")

test_longestPalindrome()
