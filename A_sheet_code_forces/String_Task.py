

if __name__=='__main__':

    s=input()

    vowels={"A","O","Y","E","U","I","a","o","y","e","u","i"}

    s=list(s)
    new_list=[]

    for i in range(len(s)):

        if s[i] not in vowels:
            # s.insert(i-1,".")
            new_list.append(".")
            new_list.append(s[i].lower())

    print(''.join(new_list))
        
