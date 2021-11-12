# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        cur = dummy = ListNode(next=head)
        while cur and cur.next:
            while cur.next and cur.next.val == val: cur.next = cur.next.next
            cur = cur.next
        return dummy.next