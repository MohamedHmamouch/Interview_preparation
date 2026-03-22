class Solution:
    def maxDifference(self, s: str) -> int:

        d={}

        max_even,min_even=0,float('inf')
        max_odd,min_odd=0,float('inf')


        for char in s:

            d[char]=1+d.get(char,0)

        
        for k,v in d.items():

            if v%2==0:

                max_even=max(max_even,v)
                min_even=min(v,min_even)

            else:
                max_odd=max(max_odd,v)
                min_odd=min(v,min_odd)

        return max(max_odd-min_even,min_odd-min_even)


        