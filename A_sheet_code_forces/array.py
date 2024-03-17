

if __name__=='__main__':

    n=int(input())
    l=list(map(int,input().split()))
    l1=[] #negatif product
    l2=[] #positif product
    l3=[] #null product
    track_negatif=0
    index=-1

    for i in l:

        if i<0:

            l1.append(i)

            if len(l1)%2==0:
                l1.pop()
                l2.append(i)
                index=len(l2)-1
                track_negatif+=1
        elif i>0:
            l2.append(i)

        else:
            l3.append(i)

    print(len(l1),*l1)
    if track_negatif%2!=0 and index!=-1:

        l3.append(l2.pop(index))
    
    print(len(l2),*l2)
    print(len(l3),*l3)



    # for v in l:

    #     count_values[v]=count_values.get(v,0)+1


    # num_negatif_l1=0
    # num_negatif_l2=0

    # for k,v in count_values.items():

    #     if k<0 and v>0:

    #         if num_negatif_l1%2==0:
    #             l1.append(k)
    #             v-=1
    #             num_negatif_l1+=1

    #         elif num_negatif_l2%2!=0:
    #             l2.append(k)
    #             v-=1
    #             num_negatif_l2+=1

    #     elif k==0 and v>0:

    #         l3.append(k)

    #     elif k>0 and v>0:
    #         l2.append(k)


    # print(len(l1),end=" ")
    # for i in l1:
    #     print(i,end=" ")
    # print("\n")
    # print(len(l2),end=" ")
    # for j in l2:
    #     print(j, end=" ")
    # print("\n")
    # print(len(l3),end=" ")
    # for x in l3:
    #     print(x,end= " ")







    
    