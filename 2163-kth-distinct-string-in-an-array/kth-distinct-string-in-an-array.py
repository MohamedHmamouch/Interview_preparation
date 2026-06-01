class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        

        mapper={}

        for char in arr:

            mapper[char]=1+mapper.get(char,0)

        

        sorted_mapper=dict(sorted(mapper.items(),key=lambda item:item[1]))
        sorted_list=[key for key,val in sorted_mapper.items() if val==1]
        print(sorted_list)
        return sorted_list[k-1] if 0<=k-1<len(sorted_list) else ""

