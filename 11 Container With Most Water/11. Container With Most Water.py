from typing import List
class Solution:
    def maxArea(self, height: List[int]) -> int:
        left_pointer = 0
        right_pointer = len(height) - 1
        max_volume = 0

        while left_pointer < right_pointer:
            if height[left_pointer] < height[right_pointer]:
                dummy_volume = (right_pointer - left_pointer) * height[left_pointer]
                left_pointer += 1
            else:
                dummy_volume = (right_pointer - left_pointer) * height[right_pointer]
                right_pointer -= 1

            if dummy_volume > max_volume:
                max_volume = dummy_volume
        
        return max_volume

def test_maxArea():
    solution = Solution()

    # Test case 1: General case with distinct heights
    assert solution.maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]) == 49, "Test case 1 failed"

    # Test case 2: All heights are equal
    assert solution.maxArea([1, 1, 1, 1, 1]) == 4, "Test case 2 failed"

    # Test case 3: Decreasing heights
    assert solution.maxArea([5, 4, 3, 2, 1]) == 6, "Test case 3 failed"

    # Test case 4: Increasing heights
    assert solution.maxArea([1, 2, 3, 4, 5]) == 6, "Test case 4 failed"

    # Test case 6: Only two heights
    assert solution.maxArea([1, 3]) == 1, "Test case 6 failed"

    # Test case 7: Larger input with varying heights
    assert solution.maxArea([1, 3, 2, 5, 25, 24, 5]) == 24, "Test case 7 failed"

    # Test case 8: Large values in input
    assert solution.maxArea([100, 1, 100, 1, 100]) == 400, "Test case 8 failed"

    print("All test cases passed!")

# Run the tests
test_maxArea()
