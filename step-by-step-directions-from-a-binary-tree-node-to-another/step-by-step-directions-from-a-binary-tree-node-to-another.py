# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        # convert tree to graph
        q = [(root, None)]
        start = None
        while q:
            cur, parent = q.pop()
            cur.par = parent
            if cur.left: q += [(cur.left, cur)]
            if cur.right: q += [(cur.right, cur)]
            if cur.val == startValue: start = cur
        
        seen = set()
        q = [(start, "")]
        while q:
            cur, path = q.pop()
            if cur.val == destValue: return path
            
            if cur.par and cur.par.val not in seen: 
                q += [(cur.par, path+"U")]
                seen.add(cur.par.val)
            if cur.left and cur.left.val not in seen: 
                q += [(cur.left, path+"L")]
                seen.add(cur.left.val)
            if cur.right and cur.right.val not in seen: 
                q += [(cur.right, path+"R")]
                seen.add(cur.right.val)