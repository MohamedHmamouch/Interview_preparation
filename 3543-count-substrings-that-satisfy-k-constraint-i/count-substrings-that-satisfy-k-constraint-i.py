class Solution:
    def countKConstraintSubstrings(self, s: str, k: int) -> int:

        l,r=0,0
        count_zeros=0
        count_ones=0

        n=len(s)
        res=0
        while r<n:

            count_ones+=1 if s[r]=='1' else 0
            count_zeros+=1 if s[r]=='0' else 0

            while count_zeros>k and count_ones>k:

                if s[l]=='1':

                    count_ones-=1

                elif s[l]=='0':

                    count_zeros-=1

                l+=1

            res+=r-l+1
            r+=1

        return res
        