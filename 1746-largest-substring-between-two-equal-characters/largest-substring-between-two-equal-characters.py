class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:

        freq={}
        
        max_substring=-1

        for index,char in enumerate(s):

            if char in freq:

                max_substring=max(max_substring,index-freq[char]-1)


            else:

                freq[char]=index

        return max_substring