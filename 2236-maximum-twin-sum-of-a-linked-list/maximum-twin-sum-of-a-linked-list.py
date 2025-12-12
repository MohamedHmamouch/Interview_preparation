# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:

        nums=[]

        curr=head

        while curr:

            nums.append(curr.val)

            curr=curr.next

        
        l,r=0,len(nums)-1

        max_sum=0

        while l<r:

            max_sum=max(max_sum,nums[l]+nums[r])
            l+=1
            r-=1


        return max_sum


        