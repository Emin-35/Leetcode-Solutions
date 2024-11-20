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

def test_removeDuplicates():
    solution = Solution()
    
    # Test case 1: No duplicates
    nums1 = [1, 2, 3, 4, 5]
    assert solution.removeDuplicates(nums1) == 5, "Test case 1 failed"
    assert nums1[:5] == [1, 2, 3, 4, 5], "Test case 1 array verification failed"
    
    # Test case 2: All duplicates
    nums2 = [2, 2, 2, 2, 2]
    assert solution.removeDuplicates(nums2) == 1, "Test case 2 failed"
    assert nums2[:1] == [2], "Test case 2 array verification failed"
    
    # Test case 3: Some duplicates
    nums3 = [1, 1, 2, 2, 3, 3, 4, 4]
    assert solution.removeDuplicates(nums3) == 4, "Test case 3 failed"
    assert nums3[:4] == [1, 2, 3, 4], "Test case 3 array verification failed"
    
    # Test case 4: Single element
    nums4 = [7]
    assert solution.removeDuplicates(nums4) == 1, "Test case 4 failed"
    assert nums4[:1] == [7], "Test case 4 array verification failed"
    
    # Test case 5: Empty array
    nums5 = []
    assert solution.removeDuplicates(nums5) == 0, "Test case 5 failed"
    assert nums5 == [], "Test case 5 array verification failed"

    print("All test cases passed!")

# Run test cases
test_removeDuplicates()
