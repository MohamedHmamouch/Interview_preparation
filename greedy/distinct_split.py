


if __name__=='__main__':

    t=int(input())

    for _ in range(t):

        n=int(input())
        s=input()

        max_val=0
        e=set()

        for i in range(len(s)):

            if s[i] not in e:

                e.add(s[i])

                val=(len(set(s[:i+1]))+len(set(s[i+1:])))

                max_val=max(max_val,val)

        print(max_val)

