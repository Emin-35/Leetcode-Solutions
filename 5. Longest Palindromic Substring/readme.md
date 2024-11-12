# Question
Given a string s, return the longest palindromic substring in s.

Example 1:
Input: s = "babad"
Output: "bab"
Explanation: "aba" is also a valid answer.

Example 2:
Input: s = "cbbd"
Output: "bb"

# Intuition
To find the longest palindromic substring, we want to expand around potential centers of palindromes. A palindrome reads the same forwards and backwards, so we can identify palindromic substrings by checking characters symmetrically around a center. There are two types of centers: 
1. A single character (for odd-length palindromes).
2. A pair of characters (for even-length palindromes).

By expanding outwards from each center, we can check for matching characters until they differ or we exceed the bounds of the string.

# Approach
1. Initialize a variable to hold the longest palindrome found so far.
2. Iterate through each character in the string and consider both odd and even-length centers:
   - For odd-length palindromes, use the current character as the center.
   - For even-length palindromes, use the current character and the next character as the center.
3. Expand outwards from the centers, checking if the characters at the left and right indices are equal:
   - If they match, update the longest palindrome if the current palindrome length exceeds the previously found longest palindrome.
   - Continue expanding until the characters no longer match or the indices go out of bounds.
4. Return the longest palindromic substring found.

# Complexity
- Time complexity: 
$$O(n^2)$$ 
(where \( n \) is the length of the input string. We potentially examine every character with two nested loops in the worst case.)

- Space complexity: 
$$O(1)$$ 
(We only use a few variables for tracking indices and the longest substring, irrespective of the input size.)


# Code
```python3 []
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

```