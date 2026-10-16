class Solution:
    def wordSubsets(self, words1: list[str], words2: list[str]) -> list[str]:

        from collections import defaultdict

        words2_freq={}
        
        current_freq={}
        for s in words2:
            current_freq={}

            for char in s:

                current_freq[char]=1+current_freq.get(char,0)


            for char in s:

                words2_freq[char]=max(current_freq[char],words2_freq.get(char,0))


        
        ans=[]
        words1_freq=defaultdict(dict)

        for s in words1:

            for char in s:

                words1_freq[s][char]=1+words1_freq[s].get(char,0)


            count=0
            for char,val in words2_freq.items():



                if char in words1_freq[s] and words1_freq[s][char]>=val:

                    count+=1

            print(count)

            
            if count==len(words2_freq):

                ans.append(s)

        print(words1_freq)

        print(words2_freq)
        return ans


