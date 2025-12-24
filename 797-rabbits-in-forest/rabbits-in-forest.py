class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        

        total=0
        freq={}
        import math

        for ans in answers:

            freq[ans]=1+freq.get(ans,0)

        print(freq)

        for k,v in freq.items():

            size_groups=k+1

            num_groups=math.ceil(v/size_groups)

            total+=size_groups*num_groups

        return total
