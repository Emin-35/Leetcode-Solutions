from typing import List
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""

        # Start with the first string as the prefix candidate
        prefix = strs[0]

        for s in strs[1:]:
            # Compare prefix with the current string
            while not s.startswith(prefix):
                # Reduce the prefix size until it matches
                prefix = prefix[:-1]
                if not prefix:
                    return ""
        
        return prefix

def test_longestCommonPrefix():
    solution = Solution()

    # Test case 1: Common prefix exists in all strings
    assert solution.longestCommonPrefix(["flower", "flow", "flight"]) == "fl", "Test case 1 failed"

    # Test case 2: No common prefix
    assert solution.longestCommonPrefix(["dog", "racecar", "car"]) == "", "Test case 2 failed"

    # Test case 3: All strings are the same
    assert solution.longestCommonPrefix(["test", "test", "test"]) == "test", "Test case 3 failed"

    # Test case 4: Only one string in the list
    assert solution.longestCommonPrefix(["single"]) == "single", "Test case 4 failed"

    # Test case 5: Empty input list
    assert solution.longestCommonPrefix([]) == "", "Test case 5 failed"

    # Test case 6: Prefix reduces to a single character
    assert solution.longestCommonPrefix(["abc", "a", "ab"]) == "a", "Test case 6 failed"

    # Test case 7: All strings share the full common prefix
    assert solution.longestCommonPrefix(["prefix", "prefix", "prefixes"]) == "prefix", "Test case 7 failed"

    # Test case 8: Empty string in the list
    assert solution.longestCommonPrefix(["", "abc", "abd"]) == "", "Test case 8 failed"

    # Test case 9: Common prefix of varying length
    assert solution.longestCommonPrefix(["interspecies", "interstellar", "interstate"]) == "inters", "Test case 9 failed"

    # Test case 10: Single character strings
    assert solution.longestCommonPrefix(["a", "a", "a"]) == "a", "Test case 10 failed"

    print("All test cases passed!")

# Run the tests
test_longestCommonPrefix()
