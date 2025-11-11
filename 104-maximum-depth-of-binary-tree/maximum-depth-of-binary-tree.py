# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:

        if not root:

            return 0
        

        depth=0
        level=1
        q=[(root,level)]

        while q:


            node,level=q.pop(0)

            if node.left:

                q.append((node.left,level+1))

            if node.right:

                q.append((node.right,level+1))


        return level