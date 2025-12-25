class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        
        if len(word1)!=len(word2):

            return False


        def same_string(s1,s2):

            s1_set=set(s1)


            for char in s2:

                if char not in s1_set:

                    return False

            return True

        word1_list=[0]*26
        word2_list=[0]*26


        for char in word1:

            word1_list[ord(char)-ord('a')]+=1
        

        for char in word2:

            word2_list[ord(char)-ord('a')]+=1

        


        return False if sorted(word1_list)!=sorted(word2_list) or not same_string(word1,word2) else True


