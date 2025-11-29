# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        
        global_min=float('-inf')
        global_max=float('inf')

        stack=[(root,global_min,global_max)]


        while stack:

            node,min_val,max_val=stack.pop()

            if node and node.val >= max_val or node.val<=min_val:

                print(node.val,max_val,min_val)

                return False


            if node.left:

                stack.append((node.left,min_val,node.val))  #[1,-inf,2]
            if node.right:

                stack.append((node.right,node.val,max_val)) #[3,2,inf]

        return True