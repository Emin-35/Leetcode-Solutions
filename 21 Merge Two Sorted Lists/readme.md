# Question
You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.

![merge_ex1](https://github.com/user-attachments/assets/e1e39936-898b-4733-95f6-52a5e6b4f900)


Example 1:


Input: list1 = [1,2,4], list2 = [1,3,4]

Output: [1,1,2,3,4,4]

Example 2:

Input: list1 = [], list2 = []

Output: []

Example 3:

Input: list1 = [], list2 = [0]

Output: [0]


# Intuition
To merge two sorted linked lists, we can leverage a two-pointer approach. By comparing the values of the nodes from both lists, we build a new merged list while maintaining the sorted order.

# Approach
1. Use a **dummy node** as a placeholder to simplify the merging process. 
2. Maintain a `tail` pointer that tracks the last node of the merged list.
3. Use two pointers, `p1` and `p2`, to traverse the two input lists (`list1` and `list2`).
4. Compare the values at `p1` and `p2`:
   - If `p1.val <= p2.val`, link `tail.next` to `p1` and move `p1` forward.
   - Otherwise, link `tail.next` to `p2` and move `p2` forward.
5. Continue until one of the lists is exhausted, then append the remaining nodes of the non-empty list.
6. Return `dummy.next`, which points to the head of the merged list.

# Complexity
- **Time Complexity:**  
  $$O(n + m)$$, where `n` is the length of `list1` and `m` is the length of `list2`. Each node is processed exactly once.

- **Space Complexity:**  
  $$O(1)$$. The merging is done in-place without using extra memory aside from pointers.

# Code
```python3 []
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()  # Placeholder node
        tail = dummy  # Points to the last node in the merged list
        
        p1, p2 = list1, list2
        
        while p1 and p2:
            if p1.val <= p2.val:
                tail.next = p1
                p1 = p1.next
            else:
                tail.next = p2
                p2 = p2.next
                
            tail = tail.next
        
        # Append remaining nodes from either list
        if p1:
            tail.next = p1
        if p2:
            tail.next = p2
        
        return dummy.next  # Skip the placeholder node
```
