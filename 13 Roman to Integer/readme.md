# Question
Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

Symbol       Value

I             1

V             5

X             10

L             50

C             100

D             500

M             1000

For example, 2 is written as II in Roman numeral, just two ones added together. 12 is written as XII, which is simply X + II. The number 27 is written as XXVII, which is XX + V + II.

Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:

I can be placed before V (5) and X (10) to make 4 and 9. 

X can be placed before L (50) and C (100) to make 40 and 90.

C can be placed before D (500) and M (1000) to make 400 and 900.

Given a roman numeral, convert it to an integer.

Example 1:

Input: s = "III"

Output: 3

Explanation: III = 3.

Example 2:

Input: s = "LVIII"

Output: 58

Explanation: L = 50, V= 5, III = 3.

Example 3:

Input: s = "MCMXCIV"

Output: 1994

Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.

# Intuition
We can convert a Roman numeral to an integer by iterating through the string from right to left. If the current character represents a smaller value than the character to its right, we subtract its value from the result. Otherwise, we add its value to the result.

# Approach
1. Initialize a dictionary to map Roman characters to their integer values.
2. Initialize the result to 0.
3. Iterate through the string from right to left.
4. If the current character represents a smaller value than the next character, subtract its value from the result and skip the next character.
5. Otherwise, add its value to the result.
6. Return the final result.

# Complexity
- Time complexity: O(n)
Where n is the length of the input string 's'. We iterate through the string once.

- Space complexity: O(1).
We use a fixed-size dictionary and a few integer variables regardless of the size of the input string.

# Code
```
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
```