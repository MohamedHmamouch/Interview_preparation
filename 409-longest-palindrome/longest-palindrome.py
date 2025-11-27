class Solution:
    def longestPalindrome(self, s: str) -> int:



        counter={}


        for char in s:

            counter[char]=1+counter.get(char,0)

        
        total=0
        max_odd=0

        for k,v in counter.items():

            if v%2==0:

                total+=v

            else:

                total+=v-1


        return total+1 if total<len(s) else total
            





        