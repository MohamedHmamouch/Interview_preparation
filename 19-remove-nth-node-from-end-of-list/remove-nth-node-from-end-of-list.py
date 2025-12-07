# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:


        length=0

        current=head

        while current:

            length+=1

            current=current.next

        print(length)

        pos=length-n

        current_index=0

        dummy=ListNode(next=head)
        prev,curr=dummy,head

        while curr and current_index!=pos:

            current_index+=1
            prev=prev.next
            curr=curr.next


        print(current_index,pos)


        prev.next=curr.next if curr.next else None

        return dummy.next

