class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        
        s=set()

        word=''.join(words)

        print(word)

        mapper={}
        for char in word:

            mapper[char]=1+mapper.get(char,0)


        for _,v in mapper.items():

            if v%len(words)!=0:

                return False

        return True 