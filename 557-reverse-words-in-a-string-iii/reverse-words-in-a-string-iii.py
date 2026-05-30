class Solution:
    def reverseWords(self, s: str) -> str:
        

        texts=s.split(' ')
        res=[]

        for word in texts:

            word_list=list(word)

            l=0
            r=len(word_list)-1

            while l<r:

                word_list[l],word_list[r]=word_list[r],word_list[l]

                l+=1
                r-=1

            res.append(''.join(word_list))

        return ' '.join(res)
            