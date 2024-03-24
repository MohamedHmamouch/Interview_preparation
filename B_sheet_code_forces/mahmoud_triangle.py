

if __name__=='__main__':

    n=int(input())

    segments=list(map(int,input().split()))

    segments.sort(reverse=True)

    i,j=0,2
    triangle=[]

    while j<len(segments):

        triangle=segments[i:j+1]

        if triangle[0]+triangle[1]>triangle[2] and triangle[1]+triangle[2]>triangle[0] and triangle[0]+triangle[2]>triangle[1]:

            print("YES")
            exit()

        else:

            i+=1
            j+=1
    print('NO')