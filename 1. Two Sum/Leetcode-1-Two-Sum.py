from typing import List
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        solution = {}

        for i in range(len(nums)):
            solution[nums[i]] = i

        for i in range(len(nums)):
            value = target - nums[i]

            if value in solution and solution[value] is not i:
                return [i, solution[value]]
        
        return []

def test_twoSum():
    solution = Solution()

    # Test case 1: Standard case with a solution.
    nums = [2, 7, 11, 15]
    target = 9
    result = solution.twoSum(nums, target)
    assert result == [0, 1], f"Expected [0, 1], but got {result}"

    # Test case 2: Case with negative numbers
    nums = [-3, 4, 3, 90]
    target = 0
    result = solution.twoSum(nums, target)
    assert result == [0, 2], f"Expected [0, 2], but got {result}"

    # Test case 3: Case where the target is a large number
    nums = [1, 2, 3, 4, 5, 6, 7, 8]
    target = 15
    result = solution.twoSum(nums, target)
    assert result == [6, 7], f"Expected [6, 7], but got {result}"

    # Test case 4: Case with no solution
    nums = [1, 2, 3, 4]
    target = 10
    result = solution.twoSum(nums, target)
    assert result == [], f"Expected [], but got {result}"

    # Test case 5: Edge case with only two elements
    nums = [1, 8]
    target = 9
    result = solution.twoSum(nums, target)
    assert result == [0, 1], f"Expected [0, 1], but got {result}"

    # Test case 6: Case where the solution is at the start of the list
    nums = [3, 4, 5, 6]
    target = 7
    result = solution.twoSum(nums, target)
    assert result == [0, 1], f"Expected [0, 1], but got {result}"

    print("All test cases passed!")

test_twoSum()
