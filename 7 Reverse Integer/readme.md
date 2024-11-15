# Question
Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.
Assume the environment does not allow you to store 64-bit integers (signed or unsigned).

Example 1:
Input: x = 123
Output: 321

Example 2:
Input: x = -123
Output: -321

Example 3:
Input: x = 120
Output: 21

# Intuition
The task is to reverse the digits of an integer while taking care of potential overflow based on the 32-bit signed integer limit. The intuitive approach is to process the number digit by digit, building the reversed result. We also need to account for negative numbers and ensure that if the reversed number exceeds the signed 32-bit integer range, we return 0.

# Approach
Sign Handling: First, determine whether the number is negative. If it is, store the sign and work with the absolute value of the number. We'll reapply the sign at the end.
Digit Reversal: We use a loop to extract the last digit of the number using modulo operation (x % 10), add that digit to the reversed number, and then remove the last digit from the original number by dividing it by 10.
Overflow Check: Before returning the result, check if the reversed number is within the 32-bit signed integer range. If it exceeds the bounds, return 0.
Final Result: Reapply the sign if necessary and return the result.
# Complexity
Time complexity: O(log n)
where n is the value of the input integer. This is because the number of digits in n determines the number of iterations we need to reverse it, and the number of digits is proportional to the logarithm of the number's value.

Space complexity:
The space complexity is O(1) 
as we are using a constant amount of extra space (only a few integer variables) regardless of the size of the input.

# Code
```python3 []
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

```