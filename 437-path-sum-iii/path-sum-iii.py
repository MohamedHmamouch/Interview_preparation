# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:

        if not root:

            return 0



        def helper(root,targeSum):


            stack=[(root,root.val,[root.val])]

            count=0


            while stack:



                node,current_sum,path=stack.pop()


                if current_sum==targetSum:

                    count+=1

                
                if node.left:

                    temp_path=path+[node.left.val]


                    stack.append((node.left,current_sum+node.left.val,temp_path))


                if node.right:

                    temp_path=path+[node.right.val]

                    stack.append((node.right,current_sum+node.right.val,temp_path))

            return count


        count=0

    
        stack=[root]
        while stack:


            node=stack.pop()


            if node:

                count+=helper(node,targetSum)

            if node.left:

                stack.append(node.left)

            if node.right:

                stack.append(node.right)

        return count

        