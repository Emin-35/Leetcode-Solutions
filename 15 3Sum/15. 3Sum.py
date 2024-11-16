from typing import List
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        final_list = []

        for index, value in enumerate(nums):
            # Skip duplicates for the first element
            if index > 0 and nums[index] == nums[index - 1]:
                continue
            
            # Use two-pointer approach
            left, right = index + 1, len(nums) - 1
            while left < right:
                current_sum = value + nums[left] + nums[right]
                
                if current_sum == 0:
                    final_list.append([value, nums[left], nums[right]])

                    # Skip duplicates for left and right
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1

                    # Move both pointers
                    left += 1
                    right -= 1
                elif current_sum < 0:
                    left += 1  # We need a larger sum, so move the left pointer to the right
                else:
                    right -= 1  # We need a smaller sum, so move the right pointer to the left

        return final_list

def test_threeSum():
    solution = Solution()

    # Test case 1: General case with multiple triplets
    assert sorted(solution.threeSum([-1, 0, 1, 2, -1, -4])) == sorted([[-1, -1, 2], [-1, 0, 1]]), "Test case 1 failed"

    # Test case 2: No triplets found
    assert solution.threeSum([1, 2, -2, -1]) == [], "Test case 2 failed"

    # Test case 3: Array with all zeros
    assert solution.threeSum([0, 0, 0, 0]) == [[0, 0, 0]], "Test case 3 failed"

    # Test case 4: Array with fewer than three elements
    assert solution.threeSum([1, -1]) == [], "Test case 4 failed"

    # Test case 5: Array with only positive numbers
    assert solution.threeSum([1, 2, 3, 4, 5]) == [], "Test case 5 failed"

    # Test case 6: Array with only negative numbers
    assert solution.threeSum([-3, -2, -1, -4]) == [], "Test case 6 failed"

    print("All test cases passed!")

# Run the tests
test_threeSum()
