class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:


        from collections import defaultdict       
        
        mapper=defaultdict(list)

        for char in strs:

            position=[0]*26

            for c in char:

                position[ord(c)-ord('a')]+=1


            mapper[tuple(position)].append(char)

        print(mapper)

        return [val for val in mapper.values()]
        