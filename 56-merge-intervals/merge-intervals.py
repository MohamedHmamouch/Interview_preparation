class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        intervals.sort(key=lambda x:x[0])
        merged_intervalls=[intervals[0]]

        #[1,7] [4,7]

        for i in range(1,len(intervals)):

            current=intervals[i] #[4,7]

            last_merged=merged_intervalls[-1]  #[1,7]


            if last_merged[1]>=current[0]: #7 > [4]

                print(last_merged[1],current[0])

                last_merged[1]=max(current[1],last_merged[1])

            else:
                merged_intervalls.append(current)


        return merged_intervalls

        