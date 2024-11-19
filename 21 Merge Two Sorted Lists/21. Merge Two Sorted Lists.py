from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        merged_listNode = ListNode()

        tail = merged_listNode

        pointer_1 = list1
        pointer_2 = list2

        while(pointer_1 and pointer_2):

            if(pointer_1.val <= pointer_2.val):
                tail.next = pointer_1
                pointer_1 = pointer_1.next

            else:
                tail.next = pointer_2
                pointer_2 = pointer_2.next

            tail = tail.next
        
        if pointer_1:
            tail.next = pointer_1
        if pointer_2:
            tail.next = pointer_2

        return merged_listNode.next

def print_list(head: Optional[ListNode]):
    result = []
    while head:
        result.append(head.val)
        head = head.next
    print(" -> ".join(map(str, result)))

def create_list(values: list) -> Optional[ListNode]:
    if not values:
        return None
    head = ListNode(values[0])
    current = head
    for value in values[1:]:
        current.next = ListNode(value)
        current = current.next
    return head

# Test cases
solution = Solution()

# Test case 1: Merging [1,2,4] and [1,3,4]
list1 = create_list([1, 2, 4])
list2 = create_list([1, 3, 4])
merged_list = solution.mergeTwoLists(list1, list2)
print("Merged List 1: ")
print_list(merged_list)

# Test case 2: Merging [1,3,5] and [2,4,6]
list1 = create_list([1, 3, 5])
list2 = create_list([2, 4, 6])
merged_list = solution.mergeTwoLists(list1, list2)
print("Merged List 2: ")
print_list(merged_list)

# Test case 3: Merging empty list with [0]
list1 = create_list([])
list2 = create_list([0])
merged_list = solution.mergeTwoLists(list1, list2)
print("Merged List 3: ")
print_list(merged_list)

# Test case 4: Merging two empty lists
list1 = create_list([])
list2 = create_list([])
merged_list = solution.mergeTwoLists(list1, list2)
print("Merged List 4: ")
print_list(merged_list)