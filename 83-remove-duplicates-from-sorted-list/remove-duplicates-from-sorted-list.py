# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:

        dummy=ListNode(next=head)
        prev=dummy
        curr=head

        while curr:

            prev=prev.next
            curr=curr.next

            while curr and curr.val==prev.val:

                curr=curr.next

            prev.next=curr

        return dummy.next
        