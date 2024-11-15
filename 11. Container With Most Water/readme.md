# Question
You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, such that the container contains the most water.

Return the maximum amount of water a container can store.

Notice that you may not slant the container.


Example 1:
![question_11](https://github.com/user-attachments/assets/4697298f-5c18-4272-a9ca-e16610a199e4)


Input: height = [1,8,6,2,5,4,8,3,7]

Output: 49

Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.

Example 2:

Input: height = [1,1]

Output: 1

# Approach
To optimize, we use the two-pointer technique:

1. Two-Pointer Technique: Initialize two pointers, one at the beginning (left_pointer) and one at the end (right_pointer) of the array.

2. Calculate Area: Calculate the area formed between the lines at these two pointers. The area is determined by the shorter line multiplied by the distance between the pointers.

3. Move Pointers: To try to find a larger area, move the pointer that points to the shorter line. This is because moving the pointer that points to the taller line wouldn't increase the height and would only reduce the width.

4. Update Maximum Area: Keep track of the maximum area found during the process.

5. Repeat: Continue moving the pointers towards each other until they meet.

# Complexity
- Time complexity:
O(n) We only traverse the array once with the two pointers moving towards each other.

- Space complexity:
O(1) We only use a constant amount of extra space for variables.

# Example

height = [1,8,6,2,5,4,8,3,7]
Initial Setup:

left_pointer = 0 (points to height 1)
right_pointer = 8 (points to height 7)
max_volume = 0

1. First Iteration:

left_pointer height = 1
right_pointer height = 7
dummy_volume = (8 - 0) * min(1, 7) = 8
max_volume is updated to 8
Move left_pointer to the right (now points to height 8)

2. Second Iteration:

left_pointer height = 8
right_pointer height = 7
dummy_volume = (8 - 1) * min(8, 7) = 49
max_volume is updated to 49
Move right_pointer to the left (now points to height 3)

3. Third Iteration:

left_pointer height = 8
right_pointer height = 3
dummy_volume = (7 - 1) * min(8, 3) = 18
max_volume remains 49
Move right_pointer to the left (now points to height 8)

4. Fourth Iteration:

left_pointer height = 8
right_pointer height = 8
dummy_volume = (6 - 1) * min(8, 8) = 40
max_volume remains 49
Move right_pointer to the left (now points to height 4)

5. Continue:

Continue moving the pointers and calculating the volume until left_pointer meets right_pointer.
Final max_volume is 49.

# Code
```
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

```
 
