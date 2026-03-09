class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        



        for i in range(int(num**0.5+1)):


            if i**2==num:

                return True

        return False