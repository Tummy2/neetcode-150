# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        
        # For mapping each node
        d = {}

        # First pass is just to create each node
        ifHead = True
        copyHead = None
        curr = head
        while curr:
            d[curr] = Node(curr.val)
            if ifHead:
                copyHead = d[curr]
                ifHead = False
            curr = curr.next

        # Second pass is to connect the nodes
        curr = head
        while curr:
            copyNext = curr.next
            copyRandom = curr.random
            d[curr].next = d.get(copyNext)
            d[curr].random = d.get(copyRandom)
            curr = curr.next

        return copyHead
    
# Time: O(N)
# Space: O(N)