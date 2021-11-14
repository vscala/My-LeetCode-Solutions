# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    
    def reverseEvenLengthGroups(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur, group_size = 0, 1
        dummy = head
        temp = []
        stack = []
        while dummy:
            cur += 1
            temp += [dummy.val]
            if cur == group_size:
                group_size += 1
                cur = 0
                stack += [temp]
                temp = []
            dummy = dummy.next
        if temp: stack += [temp]
        nstack = []
        for part in stack:
            if len(part) % 2: nstack += part
            else: nstack += part[::-1]
        cur = head
        for i in range(len(nstack)):
            cur.val = nstack[i]
            cur = cur.next
        return head