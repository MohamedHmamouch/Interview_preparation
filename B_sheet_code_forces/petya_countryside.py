
def petya_countryside(n,l:list)-> int:

    max_water=0

    for i in range(n):

        left=i-1
        right=i+1

        water_section=1

        while left>=0 and l[left]<=l[left+1]:
            water_section+=1

            left-=1

        while right<n and l[right]<=l[right-1]:

            right+=1
            water_section+=1

        max_water=max(max_water,water_section)

    return max_water

if __name__=='__main__':

    print(petya_countryside(5,[1,2,1,2,1]))    