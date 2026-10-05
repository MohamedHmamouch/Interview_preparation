class Solution:
    def leastBricks(self, walls: List[List[int]]) -> int:
        

        mapper={0:0}

        
        for wall in walls:

            total=0

            for b in wall[:-1]:

                total+=b

                mapper[total]=1+mapper.get(total,0)


        return len(walls)-max(mapper.values())