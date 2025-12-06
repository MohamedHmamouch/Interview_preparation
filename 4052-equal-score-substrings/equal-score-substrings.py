class Solution:
    def scoreBalance(self, s: str) -> bool:
        
        alphabet = {chr(i + 96): i for i in range(1, 27)}

        left_sum=0

        right_sum=sum(alphabet[char] for char in s)


        for k in range(len(s)):

            left_sum+=alphabet[s[k]]

            right_sum-=alphabet[s[k]]

            if left_sum==right_sum:

                return True

        return False