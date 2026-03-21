class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:


        mapper={}

        for num in nums1:

            mapper[num[0]]=num[1]


        for num in nums2:

            if num[0] in mapper:

                mapper[num[0]]+=num[1]

            else:

                mapper[num[0]]=num[1]

        print(mapper)

        ans=[[k,v] for k,v in mapper.items()]

        ans=sorted(ans, key=lambda x:x[0])
        print(ans)

        return ans
