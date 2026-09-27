class Solution:
    def maxDifference(self, s: str) -> int:

        max_odd,min_odd=0,float('inf')
        max_even,min_even=0,float('inf')

        freq={}


        for char in s:

            freq[char]=1+freq.get(char,0)


        for k,v in freq.items():

            if v%2==0:

                max_even=max(max_even,v)
                min_even=min(min_even,v)

            else:

                max_odd=max(max_odd,v)
                min_odd=min(min_odd,v)

        return max(max_odd-min_even,-max_even+min_odd)