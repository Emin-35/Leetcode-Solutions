# Question
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.

Example 1:

Input: nums = [-1,0,1,2,-1,-4]

Output: [[-1,-1,2],[-1,0,1]]

Explanation: 

nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.

nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.

nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.

The distinct triplets are [-1,0,1] and [-1,-1,2].

Notice that the order of the output and the order of the triplets does not matter.

Example 2:

Input: nums = [0,1,1]

Output: []

Explanation: The only possible triplet does not sum up to 0.

Example 3:

Input: nums = [0,0,0]

Output: [[0,0,0]]

Explanation: The only possible triplet sums up to 0.

# Intuition
The "3Sum" problem asks us to find all unique triplets in the array that sum to zero. To solve this efficiently, sorting the array and using a two-pointer technique allows us to systematically find valid triplets without redundant calculations.

# Approach
1. Sort the Array: Sorting simplifies finding triplets that sum to zero and helps avoid duplicates.
2. Iterate Through the Array: Use each element as a potential first element of a triplet.
    - Skip duplicates for the first element to ensure unique triplets.
3. Two-Pointer Technique: For each fixed first element, use two pointers (left and right) to find pairs that sum with the fixed element to zero.
    - If the sum is zero, add the triplet to the result and skip duplicates for the second and third elements.
    - If the sum is less than zero, move the left pointer to the right to increase the sum.
    - If the sum is greater than zero, move the right pointer to the left to decrease the sum.
4. Continue Until All Valid Triplets Are Found.

# Complexity
- Time complexity: $$O(𝑛^\2)$$
    - where 𝑛 is the length of the array. 
    - Sorting takes 𝑂(𝑛log𝑛), 
    - Two-pointer traversal for each element takes 𝑂(𝑛).

- Space complexity: O(1)
Extra space is used if we exclude the space needed for the output.

# Code
```python3 []
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

```