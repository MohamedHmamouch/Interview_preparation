class Solution:
    def maxDistance(self, nums1: List[int], nums2: List[int]) -> int:
        

        p1=0
        p2=0
        max_distance=0

        while p1<len(nums1) and p2<len(nums2):

            if nums1[p1]<=nums2[p2] and p1<=p2:

                max_distance=max(max_distance,p2-p1)

                p2+=1

            else:
                p2+=1
                p1+=1

        
        return max_distance