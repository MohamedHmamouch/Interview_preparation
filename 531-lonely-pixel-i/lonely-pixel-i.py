class Solution:
    def findLonelyPixel(self, picture: List[List[str]]) -> int:


        cols=[0]*len(picture[0])

        rows=[0]*len(picture)

        count=0

        for i in range(len(picture)):

            for j in range(len(picture[0])):


                if picture[i][j]=='B':

                    rows[i]+=1

                    cols[j]+=1


        
        for r in range(len(picture)):

            for c in range(len(picture[0])):

                if picture[r][c]=='B' and rows[r]==1 and cols[c]==1:

                    count+=1

        return count

