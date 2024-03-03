


if __name__=='__main__':

    l = input().split("|")
    new_string = input()

    for i in new_string:
        if len(l[0]) > len(l[1]):
            l[1] += i
        else:
            l[0] += i

    if len(l[0]) == len(l[1]):
        print("|".join(l))
    else:
        print("Impossible")

    

    # if len(s2)==len(s1) and len(letters_to_add)%2!=0:

    #     print("Impossible")

    # elif ((len(s2)>len(s1)) or (len(s1)>len(s2))) and len(letters_to_add)+min(len(s1),len(s2))<max(len(s1),len(s2)):
    #     print("Impossible")

    # else:

    #     min_weights=s1 if len(s1)<len(s2) else s2

    #     max_weights=s1 if len(s1)>len(s2) else s2
        
    #     stop=0
    #     for index,char in enumerate(letters_to_add):

    #         if len(max_weights)!=len(min_weights):

    #             min_weights+=char

    #         else:

    #             stop=index
                
    #             break
        
    #     remainder=len(letters_to_add[stop::])

    #     if remainder!=0 and remainder%2==0:

    #         for i, char in enumerate(letters_to_add[stop::]):

    #             if i%2==0:
    #                 min_weights+=char

    #             else:
    #                 max_weights+=char


    #     elif remainder%2!=0:
    #         print("Impossible")
    #         exit()
    
        
    #     if len(s1)<len(s2):

    #         print(f"{min_weights}|{max_weights}")

    #     else:

    #         print(f"{max_weights}|{min_weights}")



        

