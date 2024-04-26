


if __name__=='__main__':


    t=int(input())

    for _ in range(t):

        x=input()
        y=input()

        max_val=str(max(int(x),int(y)))
        min_val=str(min(int(x),int(y)))

        val_max=max_val[0]
        val_min=min_val[0]
        
        for i in range(1,len(max_val)):

            if int(val_max)>int(val_min):

                    val_max+=str(min(int(max_val[i]),int(min_val[i])))

                    val_min+=str(max(int(max_val[i]),int(min_val[i])))

            else:
                
                val_max+=str(max(int(max_val[i]),int(min_val[i])))

                val_min+=str(min(int(max_val[i]),int(min_val[i])))

        print(val_max)
        print(val_min)
             






                