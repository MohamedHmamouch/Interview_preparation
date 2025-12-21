class Solution:
    def numRabbits(self, answers: List[int]) -> int:


        freq={}

        for ans in answers:

            freq[ans]=1+freq.get(ans,0)

        total=0
        for k,v in freq.items():


            number_rabbits_in_group=k+1

            groups_to_construct=math.ceil(v/number_rabbits_in_group)

            total+=number_rabbits_in_group*groups_to_construct

        return total

        