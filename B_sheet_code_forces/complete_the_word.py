

if __name__=='__main__':


    s=input()

    if len(s)<26:
        print(-1)
        exit()



    else:

        # s=list(s)

        letter="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        d={}
        for i in letter:

            d[i]=1

        res=""

        i=0
        while i<26:

            substring=list(s[i:i+25])
            dict_copy=d
            for index,string in enumerate(substring):

                if string=="?":
 
                    for k,v in dict_copy.items():
        
                        if v==1:
        
                            substring[index]=k
                            dict_copy[k]=0
                            break
        
        
                else:
        
                    dict_copy[string]-=1

            res+=''.join(substring)

            i+=26



        print(res)



