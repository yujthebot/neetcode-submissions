# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        l3 = ListNode()
        curr = l3
        carry = 0
        while l1 or l2 or carry>0:
            first = l1.val if l1 else 0
            second =l2.val if l2 else 0
            result = first + second +carry
            if result >= 10:
                result %=10
                carry =1
            else:
                carry =0
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
            curr.next = ListNode(result)
            curr = curr.next
        return l3.next