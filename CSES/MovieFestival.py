n=int(input())
movies=[]
for i in range(n):

    a,b=map(int,input().split())
    movies.append([a,b])

movies.sort(key=lambda x:x[1])

count=0
current_end=0
for start, end in movies:

    if start >=current_end:
        count+=1
        current_end=end

print(count)