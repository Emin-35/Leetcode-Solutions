from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if (head is None or head.next is None):
            return None

        dummy = ListNode(0, head)
        slow = dummy

        for _ in range(n):
            head = head.next

        while(head):
            head = head.next
            slow = slow.next
        
        slow.next =slow.next.next

        return dummy.next

def test_removeNthFromEnd():
    solution = Solution()

    # Helper function to convert list to ListNode
    def list_to_linked_list(lst):
        dummy = ListNode(0)
        current = dummy
        for value in lst:
            current.next = ListNode(value)
            current = current.next
        return dummy.next

    # Helper function to convert ListNode to list
    def linked_list_to_list(node):
        result = []
        while node:
            result.append(node.val)
            node = node.next
        return result

    # Test case 1: Remove 2nd node from the end in [1, 2, 3, 4, 5]
    head = list_to_linked_list([1, 2, 3, 4, 5])
    result = solution.removeNthFromEnd(head, 2)
    assert linked_list_to_list(result) == [1, 2, 3, 5], "Test case 1 failed"

    # Test case 2: Remove the last node from [1, 2]
    head = list_to_linked_list([1, 2])
    result = solution.removeNthFromEnd(head, 1)
    assert linked_list_to_list(result) == [1], "Test case 2 failed"

    # Test case 3: Remove the only node in [1]
    head = list_to_linked_list([1])
    result = solution.removeNthFromEnd(head, 1)
    assert result is None, "Test case 3 failed"

    # Test case 4: Remove the 1st node from the end in [1, 2, 3]
    head = list_to_linked_list([1, 2, 3])
    result = solution.removeNthFromEnd(head, 3)
    assert linked_list_to_list(result) == [2, 3], "Test case 4 failed"

    # Test case 5: Remove the 2nd node from [1, 2, 3, 4]
    head = list_to_linked_list([1, 2, 3, 4])
    result = solution.removeNthFromEnd(head, 2)
    assert linked_list_to_list(result) == [1, 2, 4], "Test case 5 failed"

    print("All test cases passed!")

# Run the tests
test_removeNthFromEnd()
