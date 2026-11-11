class Solution:
    def minCost(self, colors: str, neededTime: list[int]) -> int:

        left=0
        right=0
        min_time=0
        count=0

        while right<len(colors):

            count=0

            while right<len(colors) and colors[left]==colors[right]:

                count+=1

                right+=1
    
            
            if count>1:

                chunk=neededTime[left:right]
                chunk.sort()

                min_time+=sum(chunk[:count-1])


            left=right

        return min_time
            

