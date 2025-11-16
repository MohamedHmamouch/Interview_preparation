# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        if not root:

            return 0
        

        current_max=-1*float('inf')

        good=0

        stack=[(root,current_max)]

        while stack:

            node,current_max=stack.pop()


            if node.val>=current_max:

                current_max=node.val

                good+=1


            if node.left:

                stack.append((node.left,max(current_max,node.left.val)))

            if node.right:

                stack.append((node.right,max(current_max,node.right.val)))

        return good