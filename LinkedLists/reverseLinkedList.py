# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        
        curr = head
        prev = None
        nextt = curr.next

        while curr and nextt:
            curr.next = prev
            prev = curr
            curr = nextt
            nextt = nextt.next

        curr.next = prev
        return curr

# Time: O(N)
# Space: O(1)