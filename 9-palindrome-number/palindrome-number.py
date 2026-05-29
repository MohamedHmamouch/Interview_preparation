class Solution:
    def isPalindrome(self, x: int) -> bool:


        if x<0:

            return False

        num_to_text=str(x)

        left,right=0,len(num_to_text)-1

        while left<right:

            if num_to_text[left]!=num_to_text[right]:

                return False


            left+=1

            right-=1

        return True