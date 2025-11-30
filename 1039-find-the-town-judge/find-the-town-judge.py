class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:


        if len(trust)==0 and n==1:

            return n


        inbound=[0]*(n+1)
        outbound=[0]*(n+1)

        for i in range(len(trust)):

            inbound[trust[i][1]]+=1

            outbound[trust[i][0]]+=1



        print(outbound)
        print(inbound)

        for j in range(len(inbound)):


            if inbound[j]==n-1 and outbound[j]==0:

                return j

        return -1       
