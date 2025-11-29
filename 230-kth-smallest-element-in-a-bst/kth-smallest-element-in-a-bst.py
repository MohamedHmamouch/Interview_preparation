# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:

        #left -> root -> right

        ans=[]
        def level_order_traversal(root):

            if not root:

                return 

            level_order_traversal(root.left)

            ans.append(root.val)

            level_order_traversal(root.right)

        
        level_order_traversal(root)

        return ans[k-1]
        