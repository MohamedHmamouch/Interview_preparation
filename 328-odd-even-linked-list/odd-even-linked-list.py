# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        if not head:

            return 

        even_head=head.next

        odd=head
        even=head.next

        while even and even.next:

            temp=even.next
            odd.next=temp
            even.next=even.next.next
            even=even.next
            odd=odd.next


        odd.next=even_head

        return head

        