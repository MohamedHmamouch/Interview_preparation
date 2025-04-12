

if __name__=='__main__':

    for _ in range(int(input())):
        n,m,x,y = map(int,input().split(' '))
        l = []
        for i in range(n):
            l.append(input())
        
        count = 0
        for i in l:
            a = i.count('..')
            b = i.count('.') - 2*a
            c = min(2*x,y)
            count += a*c + b*x
        print(count)
