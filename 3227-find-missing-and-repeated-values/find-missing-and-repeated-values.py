class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        

        seen=set()
        n=len(grid)

        total=sum([i for i in range(n**2+1)])

        matrix_total=0

        ans=[]
        current_total=0
        for i in range(n):

            for j in range(n):

                if grid[i][j] in seen:

                    ans.append(grid[i][j])

                seen.add(grid[i][j])

        

        for val in range(1,n**2+1):

            if val not in seen:

                ans.append(val)

                return ans



        return ans

