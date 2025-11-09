# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:

        if not head:
            return 


        freq={}
        curr=head


        while curr:

            freq[curr.val]=1+freq.get(curr.val,0)
            curr=curr.next

        dummy = ListNode()
        curr = dummy
        counter=0

        for key, value in freq.items():

            if value>1:
                counter+=1
                continue

            else:

                node=ListNode(val=key)

                curr.next=node

                curr=node   

        return dummy.next