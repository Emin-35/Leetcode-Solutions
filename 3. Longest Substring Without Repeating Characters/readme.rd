# Approach
1. Initialize variables:
Example: "abcabcbb"
max_length = 0:
start = 0:
subString = set():

2. Iterate through the input string "abcabcbb" using the index i:
At i = 0, we encounter 'a'. Add 'a' to the subString set. Now, subString = {'a'}.
max_length = 1
start = 0

At i = 1, we encounter 'b'. Add 'b' to the subString set. Now, subString = {'a', 'b'}.
max_length = 2
start = 0

At i = 2, we encounter 'c'. Add 'c' to the subString set. Now, subString = {'a', 'b', 'c'}.
max_length = 3
start = 0

At i = 3, we encounter 'a' again. Since 'a' is already in subString, we enter the while loop.
Remove s[0] which is 'a' in "abcabcbb"
start = 1
subString = {'b', 'c'}. check if 'a' is still in the subString
Because 'a' is not in subString we can move on outside of the while loop
Then add a back in after while loop
subString = {'a', 'b', 'c'}
max_length = 3

At i = 4, we encounter 'b' again. Since 'b' is already in subString, we enter the while loop.
Remove s[1] which is 'b' in "abcabcbb"
start = 2
subString = {'a', 'c'} check if 'b' is still in the subString
Then add b back in after while loop
subString = {'a', 'b', 'c'}.
max_length = 3

At i = 5, we encounter 'c' again. Since 'c' is already in subString, we enter the while loop.
Remove s[2] which is 'c' in "abcabcbb"
start = 3
subString = {'a', 'b'} check if 'c' is still in the subString
Then add c back in after while loop
subString = {'a', 'b', 'c'}.
max_length = 3

At i = 6, we encounter 'b'. Since 'b' is already in subString, we enter the while loop.
Remove s[3] which is 'a' in "abcabcbb"
start = 4
subString = {'b', 'c'} but 'b' is still in the subString, we need to remove s[4] which is 'b'
start = 5
subString = {'c'} and 'b' is not in the subString anymore
Then add a back in after while loop
subString = {'b', 'c'}.
max_length = 3

At i = 7, we encounter 'b' again. Since 'b' is already in subString, we enter the while loop.
Remove s[5] which is 'c' in "abcabcbb"
start = 6
subString = {'b'} but 'b' is still in the subString, we need to remove s[6] which is 'b'
subString = {} and 'b' is not in the subString anymore
start = 7
Then add a back in after while loop
subString = {'b'}.
max_length = 3

At each step, we update max_length to be the maximum length of the substring without repeating characters seen so far.
Finally, return max_length.

In this example, the longest substring without repeating characters is "abc", which has a length of 3. But because we dont need to track of the subString we can just find the maximum length of the substring

# Complexity
- Time complexity:
O(n), where n is the length of the input string 's'. This is because we iterate through the string once using a single loop.

- Space complexity:
O(n), where n is the length of the input string 's'. This is because we use a set ('subString') to store the characters of the current substring being considered. In the worst case, the set may contain all characters of the input string.

# Code
```
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        
        max_length = 0
        start = 0
        subString = set()

        for i in range(len(s)):
            
            while s[i] in subString:
                subString.remove(s[start])
                start += 1
            
            subString.add(s[i])
            max_length = max(max_length, i - start + 1)

        return max_length
```