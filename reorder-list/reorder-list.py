# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: ListNode) -> None:
        # get the halfway point using fast and slow pointers
        if not head.next: return head
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # reverse linked list starting at slow pointer
        prev, cur = None, slow.next
        slow.next = None
        while cur:
            temp = cur.next
            cur.next = prev
            prev, cur = cur, temp
        
        # combine front half of list with back half
        c1, c2 = head, prev
        while c2:
            temp = c1.next
            c1.next = c2
            c2 = c2.next
            c1.next.next = temp
            c1 = temp