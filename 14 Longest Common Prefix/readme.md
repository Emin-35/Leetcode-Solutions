# Question
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

Example 1:

Input: strs = ["flower","flow","flight"]

Output: "fl"

Example 2:

Input: strs = ["dog","racecar","car"]

Output: ""

Explanation: There is no common prefix among the input strings.

# Intuition
When solving the "longest common prefix" problem, the goal is to find the maximum common starting substring shared among all strings in the given list. The simplest way is to use one string as a reference and gradually reduce it until all strings align at the start.

# Approach
1. Assume the first string in the list is the longest common prefix.
2. Compare this prefix with each subsequent string in the list.
3. If the prefix doesn't match the beginning of a string, shorten it by removing characters from the end until it matches or becomes empty.
4. Continue this process until all strings are processed or the prefix becomes empty (indicating no common prefix).

# Complexity
- Time complexity: O(𝑆)
where 𝑆 is the sum of all characters in the list of strings. Each character is compared at most once during the prefix reduction.
- Space complexity: O(1)
as the solution uses a constant amount of extra space for the prefix variable.

# Code
```
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

```