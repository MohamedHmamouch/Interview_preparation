# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        

        current_root=root


        while current_root:


            if current_root.val==val:

                return current_root

            
            if current_root.val>val:

                current_root=current_root.left


            elif current_root.val<val:

                current_root=current_root.right

        return None