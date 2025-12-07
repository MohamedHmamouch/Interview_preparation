class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        intervals.sort(key=lambda x:x[0])

        

        merged_intervals=[intervals[0]]

        for interval in intervals:

            start=interval[0]
            end=interval[1]

            if merged_intervals[-1][1]>=start:

                merged_intervals[-1][1]=max(merged_intervals[-1][1],end)

            else:

                merged_intervals.append(interval)

        return merged_intervals