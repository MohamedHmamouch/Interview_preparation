class Solution:
    def rearrangeArray(self, nums: list[int]) -> list[int]:
        

        neg_numbers=[]

        positive_numbers=[]

        for n in nums:

            if n<0:

                neg_numbers.append(n)

            else:

                positive_numbers.append(n)


        p1=0
        p2=0
        

        res=[0]*len(nums)

        for i in range(len(res)):


            if i%2==0:

                res[i]=positive_numbers[p2]

                p2+=1

            else:

                res[i]=neg_numbers[p1]
                p1+=1

        return res