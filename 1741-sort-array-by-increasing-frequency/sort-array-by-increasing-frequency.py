class Solution:
    def frequencySort(self, nums: list[int]) -> list[int]:


        freq={}
        

        for n in nums:

            freq[n]=1+freq.get(n,0)

        
        sorted_dict=dict(sorted(freq.items(), key=lambda item:(item[1],-1*item[0])))
        
        ans=[0]*(len(nums))

        print(sorted_dict)
        p1=0
        for k,v in sorted_dict.items():


            while v!=0 and p1<len(nums):

                ans[p1]=k
                p1+=1
                v-=1

        return ans

            



        return ans