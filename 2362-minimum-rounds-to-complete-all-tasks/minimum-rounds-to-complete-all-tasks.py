class Solution:
    def minimumRounds(self, tasks: List[int]) -> int:

        freq={}

        for task in tasks:

            freq[task]=1+freq.get(task,0)


        min_round=0

        for k,v in freq.items():


            if v<2:

                return -1

            
            elif v%3==0:

                min_round+=v//3


            else:

                min_round+=v//3+1

        return min_round


        