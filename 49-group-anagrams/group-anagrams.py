class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        

        from collections import defaultdict

        freq=defaultdict(list)

        for s in strs:

            ans=[0]*27

            for char in s:

                ans[ord(char)-ord('a')]+=1


            freq[tuple(ans)].append(s)


        
        print(freq)

        return [v for _,v in freq.items()]

