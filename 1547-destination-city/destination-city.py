class Solution:
    def destCity(self, paths: List[List[str]]) -> str:


        mapper={}

        for path in paths:

            origin=path[0]
            destination=path[1]

            mapper[origin]=destination

        print(mapper)
        start=paths[0][0]


        while start in mapper:

            start=mapper[start]

        return start