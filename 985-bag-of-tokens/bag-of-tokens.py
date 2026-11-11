class Solution:
    def bagOfTokensScore(self, nums: list[int], power: int) -> int:
        

        score=0

        max_score=0

        nums.sort()

        left,right=0,len(nums)-1

        while left<=right:

            if power>=nums[left]:

                score+=1

                power-=nums[left]

                left+=1

            elif score>=1:

                power+=nums[right]
                right-=1
                score-=1

            else:

                left+=1
                right-=1

            max_score=max(max_score,score)

        return max_score