# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        

        if not root:

            return 0
        

        min_depth=float('inf')
        depth=1
        stack=[(root,depth)]

        while stack:

            node,depth=stack.pop()

            if not node.left and not node.right:

                min_depth=min(min_depth,depth)


            if node.left:

                stack.append((node.left,depth+1))

            if node.right:

                stack.append((node.right,depth+1))

        return min_depth