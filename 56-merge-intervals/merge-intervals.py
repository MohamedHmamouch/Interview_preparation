class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        intervals.sort(key=lambda x:x[0])
        print(intervals)
        ans=[intervals[0]]

        for interval in intervals:

            start=interval[0]
            end=interval[1]

            if start<=ans[-1][1]:

                ans[-1][1]=max(end,ans[-1][1])

            else:

                ans.append(interval)

        return ans

