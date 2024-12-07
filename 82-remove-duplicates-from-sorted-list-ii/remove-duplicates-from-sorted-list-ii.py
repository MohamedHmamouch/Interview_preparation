# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:

        if not head:

            return 

        repeated_val=set()

        dummy=ListNode()
        newnode=dummy
        prev=head
        curr=head.next

        while curr:

            
            if prev.val!=curr.val and prev.val not in repeated_val:

                dummy.next=prev
                dummy=dummy.next

            elif prev.val==curr.val:

                repeated_val.add(curr.val)

            prev=prev.next
            curr=curr.next
            

        if prev and prev.val not in repeated_val:

            dummy.next=prev

        elif prev and prev.val in repeated_val:

            dummy.next=prev.next

        
        return newnode.next
        