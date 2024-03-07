

if __name__=='__main__':

    mat=[]
    for _ in range(4):

        l=list(input())

        mat.append(l)

    black="#"
    for i in range(len(mat)-1):
        for j in range(len(mat)-1):
            count_black=0


            for k in range(2):

                for l in range(2):

                    if mat[i+k][j+l]==black:

                        count_black+=1
            
            count_white=4-count_black

            if count_black>=3 or count_white>=3:

                print("YES")
                exit()

    print("NO")




                


