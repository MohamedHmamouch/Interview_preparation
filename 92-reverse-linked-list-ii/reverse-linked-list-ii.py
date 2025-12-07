# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:


        ans=[]

        current=head

        while current:

            ans.append(current.val)

            current=current.next

        
        left=left-1
        right=right-1

        
        while left<=right:

            ans[left],ans[right]=ans[right],ans[left]

            left+=1

            right-=1

        dummy=ListNode()

        newhead=dummy
        for k in ans:

            dummy.next=ListNode(val=k)

            dummy=dummy.next

        return newhead.next

