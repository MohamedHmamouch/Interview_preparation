# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:


        l=[]

        while head:

            l.append(head.val)
            head=head.next

        l.sort()


        dummy=ListNode()
        current=dummy

        for n in l:

            current.next=ListNode(val=n)
            current=current.next

        return dummy.next
        