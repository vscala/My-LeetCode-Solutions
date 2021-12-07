# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []
        for i, lst in enumerate(lists):
            if lst: heappush(heap, (lst.val, i))
        cur = out = ListNode()
        while heap:
            v, i = heappop(heap)
            cur.next = ListNode(v)
            cur = cur.next
            lists[i] = lists[i].next
            if lists[i]: heappush(heap, (lists[i].val, i))
        return out.next