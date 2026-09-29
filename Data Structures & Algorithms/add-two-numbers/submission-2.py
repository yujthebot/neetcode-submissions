# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        l3 = ListNode()
        curr = l3
        carry =0
        while l1 and l2:
            if carry == 1:
                curr.next = ListNode((l1.val+l2.val+1)%10)
            else:
                curr.next = ListNode((l1.val+l2.val)%10)
            carry = 0
            
            
            if (l1.val + l2.val) >= 10:
                carry = 1
            l1 = l1.next
            l2 = l2.next
            curr = curr.next
        while l1:
            if carry == 1:
                curr.next = ListNode((l1.val+1)%10)
            else:
                curr.next = ListNode((l1.val)%10)
            carry = 0
            if (l1.val + 1)>= 10:
                carry = 1
            curr = curr.next
            l1 = l1.next
        while l2:
            if carry == 1:
                curr.next = ListNode((l2.val+1)%10)
            else:
                curr.next = ListNode((l2.val)%10)
            carry = 0
            if (l2.val + 1)>= 10:
                carry = 1
            curr = curr.next
            l2 = l2.next
        if carry == 1:
            curr.next = ListNode(1)
        return l3.next

        