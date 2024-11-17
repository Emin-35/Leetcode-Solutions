from typing import List
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums = sorted(nums)
        closest_sum = float('inf')
        
        for left in range(len(nums) - 2):
            right = left + 1
            end = len(nums) - 1

            while right < end:
                current_sum = nums[left] + nums[right] + nums[end]

                if abs(current_sum - target) < abs(closest_sum - target):
                    closest_sum = current_sum

                if current_sum == target:
                    return current_sum

                elif current_sum < target:
                    right += 1

                else:
                    end -= 1
        
        return closest_sum
    
def test_threeSumClosest():
    solution = Solution()

    # Test case 1: General case, closest sum less than target
    assert solution.threeSumClosest([-1, 2, 1, -4], 1) == 2, "Test case 1 failed"

    # Test case 2: General case, closest sum greater than target
    assert solution.threeSumClosest([1, 1, 1, 0], -100) == 2, "Test case 2 failed"

    # Test case 3: Target is exactly achievable
    assert solution.threeSumClosest([0, 1, 2], 3) == 3, "Test case 3 failed"

    # Test case 4: Large positive target
    assert solution.threeSumClosest([1, 6, 9, 14, 16, 70], 81) == 80, "Test case 4 failed"

    # Test case 5: Negative numbers with negative target
    assert solution.threeSumClosest([-5, -4, -3, -2, -1], -10) == -10, "Test case 5 failed"

    # Test case 6: Large input with duplicates
    assert solution.threeSumClosest([1, 1, 1, 1], 3) == 3, "Test case 6 failed"

    # Test case 7: Array with both positives and negatives
    assert solution.threeSumClosest([-10, -5, 2, 3, 6, 9, 11], 0) == 0, "Test case 7 failed"

    # Test case 8: Very large array
    assert solution.threeSumClosest(list(range(-1000, 1001)), 50) == 50, "Test case 8 failed"

    print("All test cases passed!")

# Run the tests
test_threeSumClosest()
