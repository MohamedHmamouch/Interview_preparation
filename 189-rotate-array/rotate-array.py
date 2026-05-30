class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k=k%len(nums)


        nums.reverse()

        print(nums,k)

        end=k-1

        left=0

        while left<end:

            nums[left],nums[end]=nums[end],nums[left]

            end-=1

            left+=1

        print(nums,'step1')
        
        left=k
        end=len(nums)-1

        print(left,end)

        while left<end:

            nums[left],nums[end]=nums[end],nums[left]

            left+=1

            end-=1


        