# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        #use two pointers moving at different speeds to calculate position
        fast = head
        slow = head
        forw = head
        n= 0
        while fast and fast.next:
            fast = fast.next.next
            n+=1
            if fast != None:
                if fast.next == None:
                    n+=1
        for i in range(n):
            slow=slow.next
        for i in range(n-1):
            forw = forw.next
        forw.next = None

        #flip the list 
        curr = slow
        prev = None
        while curr:
            nn = curr.next #save the next node
            curr.next = prev
            prev = curr
            curr = nn
        curr = head
        while prev:
            curr_next = curr.next
            prev_next = prev.next
            curr.next = prev
            prev.next = curr_next
            curr = curr_next
            prev = prev_next

        

