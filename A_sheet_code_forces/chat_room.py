

if __name__=='__main__':


    # s=input()
    # ref="hello"
    # follow=0

    # for i in range(len(s)):

    #     if s[i]==ref[follow]:

    #         follow+=1

    #     if follow==5:

    #         break

    # if follow==5:
    #     print("YES")
    # else:
    #     print("NO")
    time1_str=input()
    time2_str=input()
    hours1, minutes1 = map(int, time1_str.split(':'))

    if hours1==0:
        hours1=24
    seconds1 = hours1 * 3600 + minutes1 * 60
    
    

    hours2, minutes2 = map(int, time2_str.split(':'))

    if hours2==0:
        hours2=24

    seconds2 = hours2 * 3600 + minutes2 * 60



    # Subtract the times
    difference_seconds = abs(seconds1 - seconds2)

    # Convert the difference back to hours and minutes
    difference_hours = difference_seconds // 3600
    remaining_seconds = difference_seconds % 3600
    difference_minutes = remaining_seconds // 60

    formatted_difference = '{:02d}:{:02d}'.format(difference_hours, difference_minutes)


    print(formatted_difference)