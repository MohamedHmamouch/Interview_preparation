class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        

        r=len(arr)-1
        l=0

        while r-l>=k:

            if abs(arr[r]-x)<abs(arr[l]-x):

                l+=1

            else:

                r-=1

        return arr[l:r+1]