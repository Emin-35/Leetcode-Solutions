# Approach
1. We initialize a new linked list to store the result.
2. We iterate through the input linked lists while there are elements in either of them or there's a carry.
3. At each iteration, we calculate the sum of the current digits and the carry.
4. We update the result linked list with the last digit of the sum and update the carry.
5. We move to the next nodes in the input linked lists.
6. Finally, we return the next node of the initial node of the result linked list.

# Complexity
- Time complexity: O(max(m, n))
where m and n are the lengths of the input linked lists l1 and l2, respectively. We iterate through both linked lists once.
- Space complexity: O(max(m, n))
where m and n are the lengths of the input linked lists l1 and l2, respectively. This space is used to store the resulting linked list, which could be as long as the longer of the two input lists.

# Code
```
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
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
```