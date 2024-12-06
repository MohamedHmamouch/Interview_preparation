# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        dummy=ListNode()

        head=dummy

        while l1 and l2:

            if l1.val<=l2.val:

                dummy.next=l1

                l1=l1.next

            elif l1.val>l2.val:

                dummy.next=l2

                l2=l2.next

            
            dummy=dummy.next

        if l1:

            dummy.next=l1

        elif l2:

            dummy.next=l2

        return head.next


        