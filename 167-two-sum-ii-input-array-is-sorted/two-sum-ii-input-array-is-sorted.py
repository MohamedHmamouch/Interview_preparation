class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        l,r=0,len(numbers)-1

        while l<=r:


            if numbers[l]+numbers[r]==target:

                return [l+1,r+1]

            elif numbers[r]+numbers[l]>target:

                r-=1

            elif numbers[r]+numbers[l]<target:

                l+=1

            

            # mid=(l+r)//2

            # if numbers[l]+numbers[mid]>target:

            #     r=mid-1

            # elif numbers[mid]+numbers[r]<target:

            #     l=mid+1

            # else:

            #     return []

        