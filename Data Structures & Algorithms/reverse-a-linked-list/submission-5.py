# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = head
        while curr:
            nxt = curr.next #store the value of the next node for later
            curr.next = prev # flip the current node so that the pointer points in front
            prev = curr # update the position of prev so that it matches the next node
            curr = nxt
        return prev
            