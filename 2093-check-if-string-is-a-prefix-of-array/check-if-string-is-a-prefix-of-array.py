class Solution:
    def isPrefixString(self, s: str, words: List[str]) -> bool:

        end=0
        strs=""
        for char in words:

            strs+=char


        r=0
        
        while r<len(s) and r<len(strs) and s[r]==strs[r]:

            r+=1

        
        index=r

        print(r)
        count=0
        bucket=0
        for i in range(len(words)):

            for j in range(len(words[i])):

                count+=1

                if count==index:

                    bucket=i

                    break
        print(bucket)
        print(words[:bucket])
        return s==''.join(words[:bucket+1])