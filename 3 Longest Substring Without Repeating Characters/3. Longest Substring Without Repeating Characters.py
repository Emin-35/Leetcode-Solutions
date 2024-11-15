class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        if not s:
            return 0

        left = 0
        sub_string = set()
        max_length = 0

        for i in range(len(s)):

            while(s[i] in sub_string):
                sub_string.remove(s[left])
                left += 1
            
            sub_string.add(s[i])
            max_length = max(max_length, i - left +1)
        
        return max_length

def test_lengthOfLongestSubstring():
    solution = Solution()

    # Test case 1: Standard case with repeating characters.
    s = "abcabcbb"
    result = solution.lengthOfLongestSubstring(s)
    assert result == 3, f"Expected 3, but got {result}"

    # Test case 2: String with all unique characters
    s = "abcdef"
    result = solution.lengthOfLongestSubstring(s)
    assert result == 6, f"Expected 6, but got {result}"

    # Test case 3: Single character string
    s = "a"
    result = solution.lengthOfLongestSubstring(s)
    assert result == 1, f"Expected 1, but got {result}"

    # Test case 4: Empty string
    s = ""
    result = solution.lengthOfLongestSubstring(s)
    assert result == 0, f"Expected 0, but got {result}"

    # Test case 5: String with all identical characters
    s = "aaaaaa"
    result = solution.lengthOfLongestSubstring(s)
    assert result == 1, f"Expected 1, but got {result}"

    # Test case 7: Substring at the end of the string
    s = "abccbaefg"
    result = solution.lengthOfLongestSubstring(s)
    assert result == 6, f"Expected 5, but got {result}"
    
    # Test case 9: Special characters and numbers
    s = "123!@#123!@#"
    result = solution.lengthOfLongestSubstring(s)
    assert result == 6, f"Expected 6, but got {result}"

    print("All test cases passed!")

test_lengthOfLongestSubstring()
