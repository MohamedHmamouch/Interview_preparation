class Solution:
    def customSortString(self, order: str, s: str) -> str:
        

        mapper={}

        uncommon=""

        for char in s:

            mapper[char]=1+mapper.get(char,0)

            if char not in order:

                uncommon+=char

        

        new_str=""


        for char in order:

            if char in mapper:

                freq=mapper[char]

                while freq>0:

                    new_str+=char

                    freq-=1


        return new_str+uncommon

