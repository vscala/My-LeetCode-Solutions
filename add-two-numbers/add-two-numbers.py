# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        a = b = i = 0
        while l1:
            a += l1.val * 10 ** i
            l1 = l1.next
            i += 1
        i = 0
        while l2:
            a += l2.val * 10 ** i
            l2 = l2.next
            i += 1
        c, out = a + b, ListNode()
        cur = out
        if not c: return out
        while c:
            cur.next = ListNode(c % 10)
            cur = cur.next
            c //= 10
        return out.next
        