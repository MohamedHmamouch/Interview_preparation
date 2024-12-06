# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """

        forward=[]
        curr=head

        while curr:

            forward.append(curr.val)
            curr=curr.next

        backward=forward[::-1]

        left,right=0,len(backward)-1

        while left<=right:

            head.val=forward[left]

            head=head.next

            left+=1

            if head:

                head.val=forward[right]
                head=head.next

                right-=1


        




        