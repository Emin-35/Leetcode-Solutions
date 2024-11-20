from typing import List
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        index = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[index] = nums[i]
                index += 1
        return index

def test_removeElement():
    solution = Solution()
    
    # Test case 1: Element is present multiple times
    nums1 = [3, 2, 2, 3]
    val1 = 3
    assert solution.removeElement(nums1, val1) == 2, "Test case 1 failed"
    assert nums1[:2] == [2, 2], "Test case 1 array verification failed"

    # Test case 2: Element is not present
    nums2 = [1, 2, 3, 4, 5]
    val2 = 6
    assert solution.removeElement(nums2, val2) == 5, "Test case 2 failed"
    assert nums2[:5] == [1, 2, 3, 4, 5], "Test case 2 array verification failed"

    # Test case 3: All elements are the target value
    nums3 = [7, 7, 7, 7]
    val3 = 7
    assert solution.removeElement(nums3, val3) == 0, "Test case 3 failed"
    assert nums3[:0] == [], "Test case 3 array verification failed"

    # Test case 4: Mixed elements with some target values
    nums4 = [0, 1, 2, 2, 3, 0, 4, 2]
    val4 = 2
    assert solution.removeElement(nums4, val4) == 5, "Test case 4 failed"
    assert nums4[:5] == [0, 1, 3, 0, 4], "Test case 4 array verification failed"

    # Test case 5: Empty array
    nums5 = []
    val5 = 0
    assert solution.removeElement(nums5, val5) == 0, "Test case 5 failed"
    assert nums5 == [], "Test case 5 array verification failed"

    print("All test cases passed!")

# Run test cases
test_removeElement()
