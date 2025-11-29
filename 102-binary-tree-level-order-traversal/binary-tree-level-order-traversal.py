# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        if not root:
            return []

        q=[root]

        ans=[]
        while q:

            temp_levels=[]

            current_levels=len(q)

            for _ in range(current_levels):

                node=q.pop(0)

                temp_levels.append(node.val)

                if node.left:

                    q.append(node.left)

                if node.right:

                    q.append(node.right)

            ans.append(temp_levels)

        return ans


