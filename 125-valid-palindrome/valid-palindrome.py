class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        text=""

        for char in s:

            text+=char.lower() if char.isalnum() else ''


        left,right=0,len(text)-1

        print(text)

        while left<right:


            if text[left]!=text[right]:

                return False


            left+=1
            right-=1

        return True