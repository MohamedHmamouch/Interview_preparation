# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:


        if not head:

            return 


        node_dict={}

        current=head

        while current:

            node_dict[current.val]=1+node_dict.get(current.val,0)

            current=current.next


        print(node_dict)


        dummy=ListNode()

        newhead=dummy

        for node,freq in node_dict.items():

            if freq==1:
                dummy.next=ListNode(val=node) 

                dummy=dummy.next

        return newhead.next
        