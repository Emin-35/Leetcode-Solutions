from typing import List,Optional
# Definition for singly-linked list
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        new_node = ListNode()
        res = new_node

        total = carry = 0

        while l1 or l2 or carry:
            total = carry

            if l1:
                total += l1.val
                l1 = l1.next
            if l2:
                total += l2.val
                l2 = l2.next

            last_digit = total % 10
            carry = total // 10
            new_node.next = ListNode(last_digit)
            new_node = new_node.next

        return res.next

def test_addTwoNumbers():
    def list_to_linked_list(nums: List[int]) -> Optional[ListNode]:
        """Helper function to convert a list to a linked list."""
        if not nums:
            return None
        head = ListNode(nums[0])
        current = head
        for num in nums[1:]:
            current.next = ListNode(num)
            current = current.next
        return head

    def linked_list_to_list(node: Optional[ListNode]) -> List[int]:
        """Helper function to convert a linked list to a list."""
        result = []
        while node:
            result.append(node.val)
            node = node.next
        return result

    solution = Solution()

    # Test case 1: Two lists of equal length with no carry
    l1 = list_to_linked_list([2, 4, 3])
    l2 = list_to_linked_list([5, 6, 4])
    result = solution.addTwoNumbers(l1, l2)
    assert linked_list_to_list(result) == [7, 0, 8], f"Expected [7, 0, 8], but got {linked_list_to_list(result)}"

    # Test case 2: Two lists of different lengths
    l1 = list_to_linked_list([1, 0, 1])
    l2 = list_to_linked_list([9, 9])
    result = solution.addTwoNumbers(l1, l2)
    assert linked_list_to_list(result) == [0, 0, 2], f"Expected [0, 0, 2], but got {linked_list_to_list(result)}"

    # Test case 3: Two lists with carry over
    l1 = list_to_linked_list([9, 9, 9])
    l2 = list_to_linked_list([1])
    result = solution.addTwoNumbers(l1, l2)
    assert linked_list_to_list(result) == [0, 0, 0, 1], f"Expected [0, 0, 0, 1], but got {linked_list_to_list(result)}"

    # Test case 4: One list is empty
    l1 = list_to_linked_list([])
    l2 = list_to_linked_list([1, 2, 3])
    result = solution.addTwoNumbers(l1, l2)
    assert linked_list_to_list(result) == [1, 2, 3], f"Expected [1, 2, 3], but got {linked_list_to_list(result)}"

    # Test case 5: Both lists are empty
    l1 = list_to_linked_list([])
    l2 = list_to_linked_list([])
    result = solution.addTwoNumbers(l1, l2)
    assert linked_list_to_list(result) == [], f"Expected [], but got {linked_list_to_list(result)}"

    # Test case 6: Two lists result in a new carry at the end
    l1 = list_to_linked_list([5, 6, 7])
    l2 = list_to_linked_list([5, 4, 5])
    result = solution.addTwoNumbers(l1, l2)
    assert linked_list_to_list(result) == [0, 1, 3, 1], f"Expected [0, 1, 3, 1], but got {linked_list_to_list(result)}"

    print("All test cases passed!")

test_addTwoNumbers()
