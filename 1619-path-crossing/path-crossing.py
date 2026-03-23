class Solution:
    def isPathCrossing(self, path: str) -> bool:


        mapper={
            'N':(0,1),
            'S':(0,-1),
            'W':(-1,0),
            'E':(1,0)
        }

        start=(0,0)

        coordinates={start:1}
        current_coordinates=start

        for char in path:

            direction=mapper[char]

            current_coordinates=(current_coordinates[0]+direction[0],current_coordinates[1]+direction[1])

            if current_coordinates in coordinates:

                return True

            
            coordinates[current_coordinates]=1
        print(coordinates)
        return False
        