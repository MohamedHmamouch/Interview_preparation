from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        freq=defaultdict(list)


        for s in strs:
            ord_str=[0]*26
            for char in s:

                ord_str[ord(char)-ord('a')]+=1


            freq[tuple(ord_str)].append(s)


        return list(freq.values())

        
        