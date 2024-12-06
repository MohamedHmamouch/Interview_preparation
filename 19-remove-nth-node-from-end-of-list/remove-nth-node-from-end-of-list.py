# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        length=0

        curr=head

        while curr:

            length+=1
            curr=curr.next

        prev=ListNode(next=head)
        dummy=prev
        curr=head
        pos=length-n

        while pos:

            prev=curr
            curr=curr.next
            pos-=1

        prev.next=curr.next 

        return dummy.next
        