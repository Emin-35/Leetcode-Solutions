# Question
Given the head of a linked list, remove the nth node from the end of the list and return its head.

![remove_ex1](https://github.com/user-attachments/assets/ce986d18-6a22-4d3e-a1c3-948713808e01)

Example 1:

Input: head = [1,2,3,4,5], n = 2

Output: [1,2,3,5]

Example 2:

Input: head = [1], n = 1

Output: []

Example 3:

Input: head = [1,2], n = 1

Output: [1]

# Intuition
The goal is to remove the Nth node from the end of the list in one pass. By using two pointers, we can maintain a fixed distance between them, allowing the second pointer to identify the node before the one that needs to be removed.

# Approach
1. Use a dummy node to handle edge cases, such as when the first node needs to be removed.

2. Move the head pointer forward by n steps so that the distance between the head pointer and slow pointer is exactly n.

3. Then, move both head and slow pointers one step at a time until head reaches the end. At this point, slow will be just before the Nth node.

4. Adjust the next pointer of the slow pointer to skip the Nth node.

5. Return the list starting from dummy.next to account for the case where the first node is removed.

# Complexity
- Time complexity: O(n)
    - Since we only traverse the list once (moving the head pointer first and then both head and slow), the time complexity is linear with respect to the length of the list.

- Space complexity: O(1)
    - The space complexity is constant since we only use a few extra pointers, regardless of the size of the list.

# Code
```python3 []
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
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
```
