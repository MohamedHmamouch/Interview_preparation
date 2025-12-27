# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        if not head:

            return 


        curr=head

        length=0

        while curr:

            curr=curr.next

            length+=1

        print(length)

    
        position_to_remove=length-n

        print(position_to_remove)

        dummy=ListNode(next=head)

        current=dummy

        while position_to_remove>0:

            position_to_remove-=1

            current=current.next

        current.next=current.next.next


        return dummy.next
        