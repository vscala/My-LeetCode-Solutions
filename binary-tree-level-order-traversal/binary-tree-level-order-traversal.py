# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root: return []
        q = [(0, root)]
        out = []
        while q:
            i, cur = q.pop()
            if i < len(out): out[i] += [cur.val]
            else: out += [[cur.val]]
            if cur.right: q+=[(i+1, cur.right)]
            if cur.left: q+=[(i+1, cur.left)]
        return out