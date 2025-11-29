# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:

        if not root:

            return []


        ans=[]
        
        current_sum=0
        path=[root.val]

        stack=[(root,root.val,path)]

        while stack:


            node,current_sum,path=stack.pop()


            if not node.left and not node.right and targetSum==current_sum:

                ans.append(path)

            
            if node.left:

                new_path=path+[node.left.val]

                stack.append((node.left,current_sum+node.left.val,new_path))

            if node.right:

                new_path=path+[node.right.val]

                stack.append((node.right,current_sum+node.right.val,new_path))

        return ans