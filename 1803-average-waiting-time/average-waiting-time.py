class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:


        arrival_time=customers[0][0]

        preparation_time=customers[0][1]

        end_time=arrival_time+preparation_time

        waiting_time=end_time-arrival_time

        total_time=waiting_time


        for i in range(1,len(customers)):

            current_arrival_time=customers[i][0]

            current_end_time=customers[i][1]

            current_wait_time=0

            if current_arrival_time<=end_time:

                current_wait_time=end_time-current_arrival_time+current_end_time
                end_time=current_arrival_time+current_wait_time

            else:

                end_time=current_arrival_time+current_end_time
                current_wait_time=end_time-current_arrival_time
            
            print(i,current_wait_time,end_time)
            total_time+=current_wait_time

        return total_time/len(customers)




        