class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        odd=[]
        even=[]

        for n in nums:

            if n%2==0:

                even.append(n)

            else:

                odd.append(n)

        return even+odd