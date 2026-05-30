class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        

        ans=[]

        positive,negative=[],[]

        for n in nums:

            if n>=0:

                positive.append(n)

            else:

                negative.append(n)

        

        for i,j in zip(positive,negative):

            ans.append(i)
            ans.append(j)

        return ans