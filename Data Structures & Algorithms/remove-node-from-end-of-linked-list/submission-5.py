# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        curr = head
        tot = 0
        while curr:
            curr = curr.next
            tot+=1
        print(tot)
        curr = head
        if tot == 1:
            return curr.next
        elif tot == 2:
            if n == 2:
                return curr.next
            elif n==1:
                curr.next = None
                return curr
        elif tot == n:
            return curr.next
        
        for i in range(tot-n-1):
            curr = curr.next
        curr.next = curr.next.next

        return head

        