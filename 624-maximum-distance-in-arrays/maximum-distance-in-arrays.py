class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:


        smallest=arrays[0][0]

        largest=arrays[0][-1]

        max_val=float('-inf')

        for i in range(1,len(arrays)):


            max_val=max(abs(arrays[i][-1]-smallest),abs(arrays[i][0]-largest),max_val)

            smallest=min(arrays[i][0],smallest)

            largest=max(arrays[i][-1],largest)

        return max_val
