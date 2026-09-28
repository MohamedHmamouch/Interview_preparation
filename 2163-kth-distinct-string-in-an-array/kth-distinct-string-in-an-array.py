class Solution:
    def kthDistinct(self, arr: list[str], k: int) -> str:
        

        freq={}

        for char in arr:

            freq[char]=1+freq.get(char,0)


        ans=[key for key,val in freq.items() if val==1]


        return ans[k-1] if k<=len(ans) else ""


        
