# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:


        max_sum=float('-inf')

        q=[(root,1)]

        min_level=float('-inf')

        mapper={}

        while q:

            length=len(q)

            current_total=0

            for _ in range(length):

                node,level=q.pop(0)

                current_total+=node.val

                if node.left:

                    q.append((node.left,level+1))

                if node.right:

                    q.append((node.right,level+1))

            if current_total>=max_sum:

                max_sum=current_total
                mapper[max_sum]=level if max_sum not in mapper else min(level, mapper[max_sum])

            print(max_sum)

        return mapper[max_sum]


        