class Solution:
    def interchangeableRectangles(self, rectangles: list[list[int]]) -> int:
        

        freq={}

        counter=0

        for rectangle in rectangles:

            ratio=rectangle[0]/rectangle[1]

            if ratio in freq:

                counter+=freq.get(ratio,0)

            freq[ratio]=1+freq.get(ratio,0)

        return counter

            
