class Solution:
    def maxArea(self, height: List[int]) -> int:
        

        l,r=0,len(height)-1

        max_area=0

        while l<r:

            area=min(height[l],height[r])*(r-l)

            if area>=max_area:

                max_area=area

            

            if height[r]>=height[l]:

                l+=1
            
            else:

                r-=1

        return max_area