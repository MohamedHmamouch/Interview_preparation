# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:


        if not root1 and root2:

            return root2

        if root1 and not root2:

            return root1

        if not root1 and not root2:

            return 
        


        stack=[(root1,root2)]

        while stack:

            node1,node2=stack.pop()

            if node1 and node2:

                node1.val+=node2.val

            
            if node1.left and node2.left:

                stack.append((node1.left,node2.left))

            
            if node1.right and node2.right:

                stack.append((node1.right,node2.right))

            if node2.left and not node1.left:

                node1.left=node2.left

            if node2.right and not node1.right:

                node1.right=node2.right

        return root1