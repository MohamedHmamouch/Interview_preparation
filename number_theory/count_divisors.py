

if __name__=='__main__':

    def get_num_divisors(n):

        "returns numbers of divisors"


        i=2
        res=1

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
    
    print(get_num_divisors(6))