# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        if not l1 and l2:
            return l2
        if not l2 and l1:
            return l1

        answer = ListNode(0)
        curr = answer
        carry = 0

        while l1 and l2:
            added = l1.val + l2.val + carry
            carry = 0
            if added > 9:
                carry = 1
                added = added % 10
            curr.next = ListNode(added)
            curr = curr.next
            l1 = l1.next
            l2 = l2.next

        while l1:
            added = l1.val + carry
            carry = 0
            if added > 9:
                carry = 1
                added = added % 10
            curr.next = ListNode(added)
            curr = curr.next
            l1 = l1.next

        while l2:
            added = l2.val + carry
            carry = 0
            if added > 9:
                carry = 1
                added = added % 10
            curr.next = ListNode(added)
            curr = curr.next
            l2 = l2.next

        if carry != 0:
            curr.next = ListNode(carry)
        
        return answer.next
    
# Time: O(N)
# Space: O(N)