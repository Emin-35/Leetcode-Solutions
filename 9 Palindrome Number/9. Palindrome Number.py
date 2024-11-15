class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        
        temp = x
        reverse = 0
        
        while temp != 0:
            digit = temp % 10
            reverse = reverse * 10 + digit
            temp = temp // 10
        
        return reverse == x

def test_isPalindrome():
    solution = Solution()

    # Test case 1: Positive palindrome number
    assert solution.isPalindrome(121) == True, "Test case 1 failed"

    # Test case 2: Negative number (cannot be a palindrome)
    assert solution.isPalindrome(-121) == False, "Test case 2 failed"

    # Test case 3: Single digit number (always a palindrome)
    assert solution.isPalindrome(7) == True, "Test case 3 failed"

    # Test case 4: Non-palindrome number
    assert solution.isPalindrome(123) == False, "Test case 4 failed"

    # Test case 5: Number with trailing zeros (not a palindrome)
    assert solution.isPalindrome(100) == False, "Test case 5 failed"

    # Test case 6: Large palindrome number
    assert solution.isPalindrome(1234321) == True, "Test case 6 failed"

    # Test case 7: Large non-palindrome number
    assert solution.isPalindrome(1234567) == False, "Test case 7 failed"

    print("All test cases passed!")

# Run the tests
test_isPalindrome()
