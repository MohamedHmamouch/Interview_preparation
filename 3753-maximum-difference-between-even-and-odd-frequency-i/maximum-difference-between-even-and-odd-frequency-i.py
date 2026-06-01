class Solution:
    def maxDifference(self, s: str) -> int:
        


        freq={}

        for char in s:

            freq[char]=1+freq.get(char,0)


        
        even=sorted([v for k,v in freq.items() if v%2==0])

        odd=sorted([v for _,v in freq.items() if v%2!=0],reverse=True)


        return odd[0]-even[0]
