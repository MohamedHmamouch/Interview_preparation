class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:


        pattern_mapper={}
        word_mapper={}

        s=s.split()

        n=len(s)
        count_char=sum([1 for char in pattern])

        if n!=count_char:

            return False


        for p,char in zip(pattern,s):

            if p in pattern_mapper and pattern_mapper[p]!=char:

                return False

            if p not in pattern_mapper and char in word_mapper:
                return False


            if char not in word_mapper and p in pattern_mapper:

                return False

            if char in word_mapper and word_mapper[char]!=p:

                return False

            word_mapper[char]=p

            pattern_mapper[p]=char

        return True


        