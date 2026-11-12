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

        alter=True

        p2=0

        res=[]

        while p1<len(neg_numbers) and p2<len(positive_numbers):

            if alter:

                res.append(positive_numbers[p2])
                alter=False
                p2+=1

            else:

                res.append(neg_numbers[p1])

                alter=True

                p1+=1


        while p2<len(positive_numbers):

            res.append(positive_number[p2])
            p2+=1

        while p1<len(neg_numbers):

            res.append(neg_numbers[p1])

            p1+=1

            
        return res

            