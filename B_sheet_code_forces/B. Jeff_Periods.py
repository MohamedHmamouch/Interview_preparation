

if __name__=='__main__':
    import math

    n=int(input())
    nums=list(map(int,input().split()))

    from collections import defaultdict

    d=defaultdict(list)

    for i,v in enumerate(nums):

        d[v].append(i+1)

    pairs=[]
   
    for k,v in d.items():

            if len(v)==1:
                 pairs.append([k,0])

            else:
                 
                px=v[1]-v[0]
                is_arithmetic=True

                for i in range(1,len(v)):
                      
                    if v[i]-v[i-1]!=px:
                           
                        is_arithmetic=False
                        break

                if is_arithmetic:
                    pairs.append([k,px])

    pairs.sort(key=lambda x:x[0])

    print(len(pairs))
    for i in range(len(pairs)):
         print(pairs[i][0],pairs[i][1])
                 
                 
                

        