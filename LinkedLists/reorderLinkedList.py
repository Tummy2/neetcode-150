# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        
        # loop through entire list first to attain length
        # get the half way point
        # the second half is the second list
        # reverse the second half
        # alternate between first half and reversed second half until none
        # return head

        if not head:
            return
        if not head.next:
            return
            
        # get half point
        n = 0
        count = head
        while count:
            n += 1
            count = count.next
        half = n // 2

        # get the second half
        secondHalf = None
        curr = head
        for i in range(half):
            curr = curr.next
        secondHalf = curr

        # reverse the second half
        curr = secondHalf
        prev = None
        nextt = curr.next
        while curr and nextt:
            curr.next = prev
            prev = curr
            curr = nextt
            nextt = nextt.next
        curr.next = prev

        # alternate between both
        firstHalf = head
        secondHalf = curr
        newHead = firstHalf
        firstHalf = firstHalf.next
        curr = newHead
        alt = True
        while firstHalf and secondHalf:
            if alt:
                curr.next = secondHalf
                secondHalf = secondHalf.next
            else:
                curr.next = firstHalf
                firstHalf = firstHalf.next
            alt = not alt
            curr = curr.next
        return
    
# Time: O(N)
# Space: O(1)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# THE BETTER SOLUTION
# class Solution:
#     def reorderList(self, head: Optional[ListNode]) -> None:
#         slow, fast = head, head.next
#         while fast and fast.next:
#             slow = slow.next
#             fast = fast.next.next

#         second = slow.next
#         prev = slow.next = None
#         while second:
#             tmp = second.next
#             second.next = prev
#             prev = second
#             second = tmp

#         first, second = head, prev
#         while second:
#             tmp1, tmp2 = first.next, second.next
#             first.next = second
#             second.next = tmp1
#             first, second = tmp1, tmp2