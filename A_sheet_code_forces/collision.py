

if __name__=='__main__':
    n = int(input())
    directions = input()
    coordinates = list(map(int, input().split()))
    min_collision_time = float('inf')
    for i in range(n-1):
        if directions[i] == 'R' and directions[i+1] == 'L':
            collision_time = (coordinates[i+1] - coordinates[i]) // 2
            min_collision_time = min(min_collision_time, collision_time)
    if min_collision_time == float('inf'):
        print(-1)
    else:
        print(min_collision_time)
      		 			  			  			    	 			
    