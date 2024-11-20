# Question
Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once. The relative order of the elements should be kept the same. Then return the number of unique elements in nums.

Consider the number of unique elements of nums to be k, to get accepted, you need to do the following things:

Change the array nums such that the first k elements of nums contain the unique elements in the order they were present in nums initially. The remaining elements of nums are not important as well as the size of nums.
Return k.

Custom Judge:

The judge will test your solution with the following code:

```
int[] nums = [...]; // Input array
int[] expectedNums = [...]; // The expected answer with correct length
int k = removeDuplicates(nums); // Calls your implementation
assert k == expectedNums.length;

for (int i = 0; i < k; i++) {
    assert nums[i] == expectedNums[i];
}
```

If all assertions pass, then your solution will be accepted.

Example 1:

Input: nums = [1,1,2]

Output: 2, nums = [1,2,_]

Explanation: Your function should return k = 2, with the first two elements of nums being 1 and 2 respectively.

It does not matter what you leave beyond the returned k (hence they are underscores).

Example 2:

Input: nums = [0,0,1,1,1,2,2,3,3,4]

Output: 5, nums = [0,1,2,3,4,_,_,_,_,_]

Explanation: Your function should return k = 5, with the first five elements of nums being 0, 1, 2, 3, and 4 respectively.

It does not matter what you leave beyond the returned k (hence they are underscores).

# Intuition
The problem requires removing duplicates from a sorted array `nums` in place and returning the length of the updated array with unique elements. Since the array is sorted, duplicates will always appear consecutively. This makes it possible to use a two-pointer technique to efficiently solve the problem in linear time.

# Approach
1. **Edge Case**:  
   - If the input array `nums` is empty, return `0` as there are no elements to process.

2. **Two-Pointer Technique**:  
   - Use two pointers: 
     - `i` iterates through the array.
     - `j` keeps track of the position to place the next unique element.
   - Start `j` at `1` since the first element is always unique.
   - For each `i` starting from `1`, compare `nums[i]` with `nums[i-1]`. If they are different, assign `nums[i]` to `nums[j]` and increment `j`.

3. **Final Result**:  
   - After the loop, `j` will represent the length of the updated array with unique elements.

# Complexity
- **Time Complexity**:  
  $$O(n)$$  
  The algorithm iterates through the array once.

- **Space Complexity**:  
  $$O(1)$$  
  No additional space is used apart from a few variables.

# Code
```python3 []
from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0
        j = 1
        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:
                nums[j] = nums[i]
                j += 1
        return j
```