# Question
Given an integer array nums of length n and an integer target, find three integers in nums such that the sum is closest to target.

Return the sum of the three integers.

You may assume that each input would have exactly one solution.

Example 1:

Input: nums = [-1,2,1,-4], target = 1

Output: 2

Explanation: The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).

Example 2:

Input: nums = [0,0,0], target = 1

Output: 0

Explanation: The sum that is closest to the target is 0. (0 + 0 + 0 = 0).

# Intuition
The problem asks for the closest sum of three numbers to a given target. The first thought is that sorting the array will allow us to apply a sliding window technique with two pointers (right and end), while iterating through each element as the base pointer (left). By comparing the sum of the three numbers at these pointers to the target, we can adjust the pointers to either increase or decrease the sum until we get as close as possible to the target.

# Approach
1. Sorting the array: Begin by sorting the array, which helps in efficiently finding combinations of numbers with the sliding window approach.
2. Three pointers: Iterate over the array using three pointers:
    - left (fixed pointer) starts from the beginning and moves right through the sorted list.
    - right starts immediately after left.
    - end starts from the last element and moves left.
3. Sliding window: For each left pointer, calculate the sum of nums[left] + nums[right] + nums[end]. If the sum equals the target, return it immediately. If the sum is less than the target, increment right to try and increase the sum. If the sum is greater than the target, decrement end to reduce the sum.
4. Closest sum tracking: During the loop, maintain a variable closest_sum to track the sum that is closest to the target.
5. End result: Once all combinations are checked, return the closest sum found.

# Complexity
- Time complexity: 𝑂(𝑛^2)
O(n) , where n is the length of the input list nums. Sorting the array takes O(nlogn), and the subsequent nested loop (with two pointers) runs in O(n^2).

- Space complexity: O(1)
Assuming that the sorting is done in place and only a few extra variables are used.

# Code
```python3 []
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

```