
def count_divisor(n):

    res=1
    i=2

    while i*i<=n:

        if n%i==0:

            e=0

            while n%i==0:
                e+=1
                n/=i
            res*=(e+1)
                
        i+=1

    if n>1:
        res*=2

    return res
if __name__=='__main__':

    a,b,c=map(int,input().split())

    dic=dict()

    ans=0

    for i in range(1,a+1):

        for j in range(1,b+1):

            for k in range(1,c+1):

                product=i*k*j

                if product not in dic:

                    dic[product]=count_divisor(product)

                
                ans+=dic[product]

    print(ans)

