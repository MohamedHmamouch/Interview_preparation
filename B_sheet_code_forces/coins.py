import re

if __name__=='__main__':
    

    d={"A":0,"B":0,"C":0}

    for _ in range(3):

        s=str(input())
        
        l=re.split(r'([<>])', s)
        
        if l[1]=='>':
            d[l[0]]+=1

        else:

            d[l[2]]+=1

    if d['A']==d['B'] and d['B']==d['C']:

        print('IMPOSSIBLE')
    else:
        print(d)
        res=[0]*3
        for k,v in d.items():

            res[v]=k

        print(res)
        print(''.join(res))



