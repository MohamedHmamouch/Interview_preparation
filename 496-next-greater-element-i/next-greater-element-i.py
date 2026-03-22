class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:

        mapper={}

        for i in range(len(nums2)):

            for j in range(i+1,len(nums2)):

                if nums2[j]>nums2[i]:

                    mapper[nums2[i]]=nums2[j]
                    break

        ans=[]

        for n in nums1:

            if n in mapper:

                ans.append(mapper[n])

            else:

                ans.append(-1)

        return ans